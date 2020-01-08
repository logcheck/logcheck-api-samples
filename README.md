# LogCheck API: Getting Started

## Prerequisites
- A **terminal program** (e.g. Terminal, iTerm) running a **sh-compatible shell** (e.g. Bash, ZSH)
- A **scripting language**. Our examples use Python and Ruby, but you may use any scripting language that
    supports making an HTTP GET requests with basic HTTP authentication.

## Getting Started

### 1. Request API Access
Complete [the sign-up
form](https://www.logcheck.com/logchecks-api-how-to-fetch-data-from-your-logbooks/)
and a LogCheck team member will help you get started.

### 2. Generate credentials
- Log in to the website [https://www.logcheckapp.com](https://www.logcheckapp.com/login)
- In the drop down under your name, select `Settings`
- Select the `API Tokens` tab on the left
- Select the `Generate a new token` button.  (If the button is disabled, you
    need to complete [the sign-up
    form](https://www.logcheck.com/logchecks-api-how-to-fetch-data-from-your-logbooks/)
    to enable API access for your user account.)
- Leave the resulting page open until **step 4**

### 3. Clone this repo

From your shell:

```sh
cd ~
git clone git@github.com:logcheck/logcheck-api-samples.git
cd logcheck-api-samples
```

### 4. Set up environment
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

**Prerequisites**: [python3](https://www.python.org/downloads/) and [pip3](https://pip.pypa.io/en/stable/installing/)

```bash
cd python/
pip3 install jsonapi-client
python3 client.py
```
