import json

# Mock data
PRODUCTS = json.load(open('backend/data/products.json'))
INGREDIENTS = json.load(open('backend/data/ingredients.json'))
SALES = json.load(open('backend/data/sales.json'))

# Simple function to find relevant product info
def get_augmented_info(product_id):
    try:
        product = next((p for p in PRODUCTS if p["id"] == product_id), None)
        if not product:
            return "Product not found."

        augmented_description = product["description"]

        # Add information about ingredients
        for ingredient in product["ingredients"]:
            ingredient_info = next((i for i in INGREDIENTS if i["name"].lower() == ingredient.lower()), None)
            if ingredient_info:
                augmented_description += f"\n- {ingredient}: {ingredient_info['properties']} Effects: {', '.join(ingredient_info['common_effects'])}"

        # Add sales data if available
        sales_data = next((s for s in SALES if s["product_id"] == product_id), None)
        if sales_data:
            total_sales = sum(day["units_sold"] for day in sales_data["daily_sales"])
            augmented_description += f"\n- Total Units Sold: {total_sales}"

        return str(augmented_description) if augmented_description else "No additional information available."
    except Exception as e:
        print(f"Error in get_augmented_info: {e}")
        return "Error retrieving augmented information."


def get_llama_recommendation(user_interest: str):
    # Find product based on interest (simple matching)
    recommended_products = []
    for product in PRODUCTS:
        if user_interest.lower() in product["name"].lower() or user_interest.lower() in product["description"].lower():
            augmented_info = get_augmented_info(product["id"])
            # Only add to recommendations if augmented_info is valid
            recommended_products.append({
                "name": product["name"],
                "augmented_info": augmented_info
            })

    if not recommended_products:
        return "Sorry, we couldn't find products matching your interest."

    return recommended_products
