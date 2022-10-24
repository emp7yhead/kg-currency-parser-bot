# kg-currency-parser-bot

[![Tests and linter](https://github.com/emp7yhead/kg-currency-parser-bot/actions/workflows/main.yml/badge.svg)](https://github.com/emp7yhead/kg-currency-parser-bot/actions/workflows/main.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/499160adca67df16843a/maintainability)](https://codeclimate.com/github/emp7yhead/kg-currency-parser-bot/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/499160adca67df16843a/test_coverage)](https://codeclimate.com/github/emp7yhead/kg-currency-parser-bot/test_coverage)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![Telegram](https://img.shields.io/badge/-telegram-red?color=white&logo=telegram&logoColor=black)](https://t.me/kg_currency_bot)

https://t.me/kg_currency_bot

Bot for helping you know latest currency exchange rate for the Kyrgyz som.

Now bot gives information for:

- KGS -> USD
- KGS -> EUR
- KGS -> RUB

## Dependencies

- python = "^3.10"
- aiogram = "3.0.0b5"
- python-dotenv = "^0.21.0"
- pandas = "^1.5.1"
- requests = "^2.28.1"
- lxml = "^4.9.1"

### dev dependencies

- pytest = "^7.1.3"
- wemake-python-styleguide = "^0.17.0"

## Installation for user

In telegram in search field just type `Actual KG currency`

or just follow the link `https://t.me/kg_currency_bot`

## Installation for dev

```bash
git clone git@github.com:emp7yhead/kg-currency-parser-bot.git
cd kg-currency-parser-bot
make install
```

## Contribution

Feel free to contribute (pull requests and issues are welcome).
