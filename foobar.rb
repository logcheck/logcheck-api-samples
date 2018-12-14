# frozen_string_literal: true
require 'dotenv/load'
require 'csv'
require 'pry'
require 'rest-client'
require 'base64'
require 'json'

def encode_credentials(user_name, password)
  "Basic #{::Base64.strict_encode64("#{user_name}:#{password}")}"
end

def process(uuid)
  api_base_uri = 'https://www.logcheckapp.com/api/v1/'
  records_path = "logs/#{uuid}/records"
  foobar = api_base_uri + records_path

  user_name = ENV['TOKEN_ID']
  password = ENV['SECRET_KEY']

  response = RestClient.get foobar, {
    params: { published_since: '2018-12-13T00:00:00Z' },
    Authorization: encode_credentials(user_name, password)
  }

  print_response(response)
rescue Exception => ex
  puts ex.response
end

def print_response(response)
  puts "user_recorded\t\t\tvalue"
  puts "-------------\t\t\t-----"
  
  as_json = JSON.parse(response)
  as_json['data'].each do |record|
    attrs = record['attributes']

    value = attrs['value']
    recorded_at = Time.parse(attrs['user_recorded'])

    puts "#{recorded_at.strftime('%D %r')}\t\t#{value}"
  end
end

schema_file = 'SJC35_Rounds_Schema.txt'
csv_options = {
  col_sep: "\t",
  headers: true,
  header_converters: :symbol
}

counter = 0
CSV.foreach(schema_file, csv_options) do |row|
  process('6d7fa70f802f411a9ea208ed1d17ebf9') if counter == 0
  counter += 1
end

