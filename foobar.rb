# frozen_string_literal: true
require 'dotenv/load'
require 'csv'
require 'pry'

def process(uuid)
  api_base_uri = 'https://www.logcheckapp.com/api/v1/'
  records_path = "logs/#{uuid}/records"
  foobar = api_base_uri + records_path

  puts foobar
end

schema_file = 'SJC35_Rounds_Schema.txt'
csv_options = { col_sep: "\t", headers: true, header_converters: :symbol }

CSV.foreach(schema_file, csv_options) do |row|
  process(row[:uuid])
end

