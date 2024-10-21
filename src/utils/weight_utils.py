import re

def convert_weight_to_grams(weight):

    if weight is not None:

        match = re.search(r'(\d+(\.\d+)?)\s*(kg|g|pounds|lbs)', weight, re.IGNORECASE)

        if match:

            number = float(match.group(1))
            unit = match.group(3).lower()

            if unit == 'kg':

                return number * 1000
            
            elif unit in ['pounds', 'lbs']:

                return number * 453.592
            
            return number
    
        return None
    
    return weight


def convert_weight_to_kg(weight):

    if weight is not None:

        match = re.search(r'(\d+(\.\d+)?)\s*(kg|g|pounds|lbs)', weight, re.IGNORECASE)

        if match:

            weight = float(match.group(1))
            unit = match.group(3).lower()

            if unit == 'kg':

                return f"{weight:.2f} kg"

            elif unit in ['pounds', 'lbs']:

                weight = weight * 453.592

            weight = weight / 1000

            return f"{weight:.2f} kg"
        
        return None
    
    return weight


def calculate_average_weight(weight_gpt, weight_bestbuy):

    weight_gpt = convert_weight_to_grams(weight_gpt)
    weight_bestbuy = convert_weight_to_grams(weight_bestbuy)

    if weight_gpt is not None and weight_bestbuy is not None:

        weight_in_g = (weight_gpt + weight_bestbuy) / 2

    else:

        weight_in_g = weight_gpt if weight_gpt else (weight_bestbuy if weight_bestbuy else None)

        if weight_in_g is None:

            return None

    if weight_in_g:

        weight_in_kg = weight_in_g / 1000

        return f"{weight_in_kg:.2f} kg"

    return None