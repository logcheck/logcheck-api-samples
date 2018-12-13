# frozen_string_literal: true
require 'dotenv/load'
require 'csv'
require 'pry'
require 'rest-client'
require 'base64'

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
rescue Exception => ex
  binding.pry
end

schema_file = 'SJC35_Rounds_Schema.txt'
csv_options = {
  col_sep: "\t",
  headers: true,
  header_converters: :symbol
}

counter = 0
CSV.foreach(schema_file, csv_options) do |row|
  process(row[:uuid]) if counter == 0
  counter += 1
end

