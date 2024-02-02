import json
import pandas as pd

# Function to flatten nested json
def flatten_json(nested_json):
    out = {}
    # function that actually does the flattening
    def flatten(x, name=''):
        # This is just for logging, ignore it
        print(f'name: {name} x: {x}')
        # If the Nested key-value is a list e.g. multiple key value pairs
        if type(x) is dict:
            # Then for each key value pair for call flatten recursively because the value might be another list
            # for example "AAPL": {"price": 150, "volume": 1000000} <- key is AAPL but the value is a list or dictionary
            for a in x:
                flatten(x[a], name + a + '_')
        # If the Nested key-value is not a list of key value pairs then just add it to the out dictionary
        else:
            out[name[:-1]] = x

    json_object = json.loads(nested_json)
    flatten(json_object)
    return out


def create_dataframe_for_stock_data_table(json_obj, stock_symbol):
    data = {
        'StockSymbol': stock_symbol,
        'PriceCurrency': json_obj[f'{stock_symbol}_price_currency'],
        'StockPrice': json_obj[f'{stock_symbol}_stock_price'],
        'FairPriceDCFEBITDA10': json_obj[F'{stock_symbol}_valuation_fair_price_dcf_ebitda_10'],
        'FairPriceDCFEBITDA5': json_obj[F'{stock_symbol}_valuation_fair_price_dcf_ebitda_5'],
        'FairPriceDCFGrowth10': json_obj[F'{stock_symbol}_valuation_fair_price_dcf_growth_10'],
        'FairPriceDCFGrowth5': json_obj[F'{stock_symbol}_valuation_fair_price_dcf_growth_5'],
        'FairPriceDDMMulti': json_obj[F'{stock_symbol}_valuation_fair_price_ddm_multi'],
        'FairPriceDDMStable': json_obj[f'{stock_symbol}_valuation_fair_price_ddm_stable'],
        'FairPriceEPV': json_obj[f'{stock_symbol}_valuation_fair_price_epv'],
        'FairPriceEVEBITDA': json_obj[f'{stock_symbol}_valuation_fair_price_ev_ebitda'],
        'FairPricePE': json_obj[f'{stock_symbol}_valuation_fair_price_pe'],
        'FairPricePeterLynch': json_obj[f'{stock_symbol}_valuation_fair_price_peter_lynch'],
        'UpsideDCFEBITDA10': json_obj[f'{stock_symbol}_valuation_upside_dcf_ebitda_10'],
        'UpsideDCFEBITDA5': json_obj[f'{stock_symbol}_valuation_upside_dcf_ebitda_5'],
        'UpsideDCFGrowth10': json_obj[f'{stock_symbol}_valuation_upside_dcf_growth_10'],
        'UpsideDCFGrowth5': json_obj[f'{stock_symbol}_valuation_upside_dcf_growth_5'],
        'UpsideDDMMulti': json_obj[f'{stock_symbol}_valuation_upside_ddm_multi'],
        'UpsideDDMStable': json_obj[f'{stock_symbol}_valuation_upside_ddm_stable'],
        'UpsideEPV': json_obj[f'{stock_symbol}_valuation_upside_epv'],
        'UpsideEVEBITDA': json_obj[f'{stock_symbol}_valuation_upside_ev_ebitda'],
        'UpsidePE': json_obj[f'{stock_symbol}_valuation_upside_pe'],
        'UpsidePeterLynch': json_obj[f'{stock_symbol}_valuation_upside_peter_lynch'],
        'Beta': json_obj[f'{stock_symbol}_wacc_components_beta'],
        'CostOfDebt': json_obj[f'{stock_symbol}_wacc_components_cost_of_debt'],
        'CostOfEquity': json_obj[f'{stock_symbol}_wacc_components_cost_of_equity'],
        'WACC': json_obj[f'{stock_symbol}_wacc_components_wacc']
    }
    df = pd.DataFrame(data, index=[0])
    return df

