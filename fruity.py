import argparse
import json
import sys

import requests

class FruitAPI:
    """Class to handle fruit lookup operations with FruityVice API"""

    def __init__(self, api_url="https://www.fruityvice.com/api/fruit"):
        """
        Initialise the FruitAPI class
        Args:
            api_url: URL used for the API, defaults to FruityVice API
        """
        self.api_url = api_url

    def get_fruit_info(self, fruit_name):
        """
        Fetch details about specific fruit from the API
        Args:
            fruit_name: Name of the fruit to look up
        Returns:
            Fruit details in JSON format or None (if the fruit is not found/the service is unavailable)
        """
        try:
            response = requests.get(f"{self.api_url}/{fruit_name}")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error: Couldn't retrieve fruit data - {e}", file=sys.stderr)
            return None

    def format_display(self, fruit_data, output_format="human"):
        """
        Format fruit data according to the specified output format - either "human" or "machine"
        Args:
            fruit_data: The fruit data retrieved from the API
            format: The specified output format
        Returns:
            A string containing the formatted output, or JSON string (if format is "machine")
        """
        if output_format.lower() == "machine":
            result = {
                "name": fruit_data.get("name"),
                "id": fruit_data.get("id"),
                "family": fruit_data.get("family"),
                "sugar": fruit_data.get("nutritions", {}).get("sugar"),
                "carbohydrates": fruit_data.get("nutritions", {}).get("carbohydrates"),
            }
            return json.dumps(result)
        else:
            return (
                f"Fruit Name: {fruit_data.get('name')}\n"
                f"ID: {fruit_data.get('id')}\n"
                f"Family: {fruit_data.get('family')}\n"
                f"Sugar: {fruit_data.get('nutritions', {}).get('sugar')}g\n"
                f"Carbohydrates: {fruit_data.get('nutritions', {}).get('carbohydrates')}g"
            )


def main():
    """Parses command line arguments and displays fruit information"""
    parser = argparse.ArgumentParser(description="Look up information about a fruit from the FruityVice API")
    parser.add_argument("fruit", help="Name of the fruit to look up")
    parser.add_argument("--format", choices=["human", "machine"], default="human", help="Output format (human-readable text or machine-readable JSON)")
    parser.add_argument("--api-url", default="https://www.fruityvice.com/api/fruit", help="Custom API URL (defaults to https://www.fruityvice.com/api/fruit)")
    args = parser.parse_args()

    fruit_obj = FruitAPI(args.api_url) 
    fruit_data = fruit_obj.get_fruit_info(args.fruit)

    if not fruit_data:
        print(f"Error: Fruit not found or service unavailable")
        sys.exit(1)

    print(fruit_obj.format_display(fruit_data, args.format))


if __name__ == "__main__":
    main()