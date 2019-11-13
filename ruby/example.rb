# frozen_string_literal: true
require 'dotenv/load'
require 'pry'
require 'rest-client'
require 'base64'
require 'json'

API_BASE_URI = ENV['API_BASE_URI']

USER_NAME = ENV['TOKEN_ID']
PASSWORD = ENV['SECRET_KEY']

def print_response(json_response)
  json_response['data'].each do |record|
    print_record(record)
  end
end

def print_record(json_record)
  attrs = json_record['attributes']

  value = attrs['value']
  recorded_at = Time.parse(attrs['user_recorded'])

  puts "#{recorded_at.strftime('%D %r')}\t\t#{value}"
end

# Setup
log_uuid = '762816f4e1354f0fa3dcdf7ab26b059b'
records_path = "logs/#{log_uuid}/records"
request_uri = "#{API_BASE_URI}/#{records_path}"

# Make the request
response = RestClient.get request_uri, {
  params: { published_since: '2019-05-02T00:00:00Z' },
  Authorization: "Basic #{::Base64.strict_encode64("#{USER_NAME}:#{PASSWORD}")}"
}

# Print the response
puts "user_recorded\t\t\tvalue"
puts "-------------\t\t\t-----"
print_response(JSON.parse(response))
