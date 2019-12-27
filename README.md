# LogCheck API: Getting Started

## Prerequisites
- A **terminal program** (e.g. Terminal, iTerm) running a **sh-compatible shell** (e.g. Bash, ZSH)
- A **scripting language**. Our examples use Python and Ruby, but you may use any scripting language that
    supports making an HTTP GET requests with basic HTTP authentication.

## Getting Started

### 0. Generate credentials
- Email support to request API access
- Log in to the website [https://www.logcheckapp.com](https://www.logcheckapp.com/login)
- In the drop down under your name, select `Settings`
- Select the `API Tokens` tab on the left
- Select the `Generate a new token` button
- Leave the resulting page open until **step 2**

### 1. Clone this repo

From your shell:

```sh
cd ~
git clone git@github.com:logcheck/logcheck-api-samples.git
cd logcheck-api-samples
```

### 2. Set up environment
- Set `TOKEN_ID` and `SECRET_KEY` from **step 0** as environment variables

```sh
touch credentials.env
echo "export TOKEN_ID='<paste TOKEN_ID>'" >> credentials.env
echo "export SECRET_KEY='<paste SECRET_KEY>'" >> credentials.env
source credentials.env
```

Note that you will need to `source credentials.env` again on subsequent shell
sessions.

Please also note that this repo contains a `.gitignore` file which excludes
`credentials.env` from source control. Be sure to add this file to your
own future repos to avoid leaking your LogCheck API credentials.

## Example Usage: Ruby

**Prerequisites**: [ruby](https://www.ruby-lang.org/en/documentation/installation/) and [bundler](https://bundler.io/)

```bash
cd ruby/
bundle install
ruby example.rb
```

## Example Usage: Python

**Prerequisites**: [python3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/)

```bash
cd python/
pip install jsonapi-client
python3 client.py
```
