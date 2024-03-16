from __future__ import print_function
import cloudmersive_currency_api_client
from cloudmersive_currency_api_client.rest import ApiException
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

Bootstrap5(app)

app.config['SECRET_KEY'] = 'any_secret_key'

# Configure API key authorization: Apikey
configuration = cloudmersive_currency_api_client.Configuration()
configuration.api_key['Apikey'] = 'your_api_key'

# create an instance of the API class
api_instance = cloudmersive_currency_api_client.CurrencyExchangeApi(
    cloudmersive_currency_api_client.ApiClient(configuration))

# Get a list of available currencies and corresponding countries
api_response_all_curr = api_instance.currency_exchange_get_available_currencies()

curr_code_list = api_response_all_curr.currencies

code_with_country_list = []
for currency in curr_code_list:
    code_with_country = currency.country_name + ", " + currency.iso_currency_code
    code_with_country_list.append(code_with_country)


class MyForm(FlaskForm):
    from_field = SelectField(label="From", choices=code_with_country_list, validators=[DataRequired()])
    to_field = SelectField(label="To",  choices=code_with_country_list, validators=[DataRequired()])
    money = IntegerField(label="Amount", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


@app.route('/', methods=['GET', 'POST'])
def home():
    form = MyForm()
    post = False
    if form.validate_on_submit():
        post = True
        source_currency_entered = form.from_field.data.split(", ")[1]
        destination_currency_entered = form.to_field.data.split(", ")[1]
        money = form.money.data
        conversion_data = conversion(source_currency_entered, destination_currency_entered, money)
        currency_converted = conversion_data[0]
        exchange_rate_calculated = float(conversion_data[1])
        return render_template('index.html', form=form, curr=currency_converted,
                               rate=round(exchange_rate_calculated, 4), post=post)
    return render_template('index.html', form=form, post=post)


def conversion(source, destination, money):

    source = source  # str | Source currency three-digit code (ISO 4217), e.g. USD, EUR, etc.
    destination = destination  # str | Destination currency three-digit code (ISO 4217), e.g. USD, EUR, etc.
    source_price = money  # float | Input price, such as 19.99 in source currency

    # Converts a price from the source currency into the destination currency
    api_response_convert = api_instance.currency_exchange_convert_currency(source, destination, source_price)
    converted_price = api_response_convert.formatted_price_as_string

    # Gets the exchange rate from the source currency into the destination currency
    api_response_rate = api_instance.currency_exchange_get_exchange_rate(source, destination)
    exchange_rate = api_response_rate.exchange_rate

    return [converted_price, exchange_rate]


if __name__ == "__main__":
    app.run(debug=True, port=5003)
