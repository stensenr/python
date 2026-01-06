"""
Simple Recommendation System
Demonstrates collaborative filtering and similarity metrics
"""

import json
from collections import defaultdict


class RecommendationSystem:
    """A simple recommendation system based on user purchase history."""
    
    def __init__(self):
        """Initialize the recommendation system."""
        self.users = {}  # {user_id: set of product_ids}
        self.products = {}  # {product_id: product_name}
        self.product_users = defaultdict(set)  # {product_id: set of user_ids who bought it}
    
    def add_user(self, user_id, username):
        """Add a new user to the system."""
        if user_id not in self.users:
            self.users[user_id] = set()
            print(f"✓ Added user: {username} (ID: {user_id})")
        else:
            print(f"User {user_id} already exists!")
    
    def add_product(self, product_id, product_name):
        """Add a new product to the system."""
        self.products[product_id] = product_name
        print(f"✓ Added product: {product_name} (ID: {product_id})")
    
    def add_purchase(self, user_id, product_id):
        """Record a user purchase."""
        if user_id not in self.users:
            print(f"Error: User {user_id} not found!")
            return
        if product_id not in self.products:
            print(f"Error: Product {product_id} not found!")
            return
        
        self.users[user_id].add(product_id)
        self.product_users[product_id].add(user_id)
        print(f"✓ Purchase recorded: User {user_id} bought {self.products[product_id]}")
    
    def get_user_purchases(self, user_id):
        """Get list of products purchased by a user."""
        if user_id not in self.users:
            print(f"User {user_id} not found!")
            return []
        
        purchases = self.users[user_id]
        print(f"\nUser {user_id} purchases:")
        for product_id in purchases:
            print(f"  - {self.products[product_id]}")
        return purchases
    
    def jaccard_similarity(self, set1, set2):
        """Calculate Jaccard similarity between two sets.
        
        Jaccard similarity = |intersection| / |union|
        Range: 0 (no overlap) to 1 (identical sets)
        
        Args:
            set1: First set
            set2: Second set
        
        Returns:
            Similarity score between 0 and 1
        """
        if not set1 and not set2:
            return 0.0
        
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        
        return intersection / union if union > 0 else 0.0
    
    def find_similar_users(self, user_id, top_n=3):
        """Find users most similar to the given user.
        
        Args:
            user_id: The user to find similarities for
            top_n: Number of similar users to return
        
        Returns:
            List of (user_id, similarity_score) tuples
        """
        if user_id not in self.users:
            print(f"User {user_id} not found!")
            return []
        
        user_purchases = self.users[user_id]
        similarities = []
        
        # Calculate similarity with all other users
        for other_user_id in self.users:
            if other_user_id != user_id:
                other_purchases = self.users[other_user_id]
                similarity = self.jaccard_similarity(user_purchases, other_purchases)
                similarities.append((other_user_id, similarity))
        
        # Sort by similarity (highest first) and return top N
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:top_n]
    
    def recommend_products(self, user_id, top_n=3):
        """Recommend products to a user based on similar users' purchases.
        
        Args:
            user_id: The user to make recommendations for
            top_n: Number of products to recommend
        
        Returns:
            List of recommended product IDs
        """
        if user_id not in self.users:
            print(f"User {user_id} not found!")
            return []
        
        user_purchases = self.users[user_id]
        recommendations = defaultdict(float)
        
        # Find similar users
        similar_users = self.find_similar_users(user_id, top_n=5)
        
        # Collect products from similar users
        for similar_user_id, similarity in similar_users:
            similar_user_purchases = self.users[similar_user_id]
            
            # Add products that the target user hasn't bought yet
            for product_id in similar_user_purchases:
                if product_id not in user_purchases:
                    # Weight by similarity score
                    recommendations[product_id] += similarity
        
        # Sort by recommendation score
        sorted_recommendations = sorted(
            recommendations.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        return [product_id for product_id, score in sorted_recommendations[:top_n]]
    
    def get_products_bought_together(self, product_id, top_n=3):
        """Find products frequently bought with the given product.
        
        Args:
            product_id: The product to find associations for
            top_n: Number of associated products to return
        
        Returns:
            List of (product_id, co-occurrence_count) tuples
        """
        if product_id not in self.products:
            print(f"Product {product_id} not found!")
            return []
        
        # Get users who bought this product
        users_who_bought = self.product_users[product_id]
        
        # Count co-occurrences with other products
        co_occurrences = defaultdict(int)
        
        for user_id in users_who_bought:
            user_purchases = self.users[user_id]
            for other_product_id in user_purchases:
                if other_product_id != product_id:
                    co_occurrences[other_product_id] += 1
        
        # Sort by frequency
        sorted_products = sorted(
            co_occurrences.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        return sorted_products[:top_n]



def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("     RECOMMENDATION SYSTEM")
    print("="*50)
    print("1. Add user")
    print("2. Add product")
    print("3. Record purchase")
    print("4. View user purchases")
    print("5. Find similar users")
    print("6. Get recommendations for user")
    print("7. Find products bought together")
    print("8. View all users")
    print("9. View all products")
    print("10. Save data")
    print("11. Load data")
    print("12. Exit")
    print("="*50)


def save_system(rec_sys, filename="rec_system_data.json"):
    """Save the recommendation system to a file."""
    data = {
        "users": {user_id: list(products) for user_id, products in rec_sys.users.items()},
        "products": rec_sys.products,
        "product_users": {prod_id: list(users) for prod_id, users in rec_sys.product_users.items()}
    }
    
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"✓ Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data: {e}")


def load_system(rec_sys, filename="rec_system_data.json"):
    """Load the recommendation system from a file."""
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        
        rec_sys.users = {user_id: set(products) for user_id, products in data["users"].items()}
        rec_sys.products = data["products"]
        rec_sys.product_users = defaultdict(set, {
            prod_id: set(users) for prod_id, users in data["product_users"].items()
        })
        
        print(f"✓ Data loaded from {filename}")
        print(f"  Users: {len(rec_sys.users)}, Products: {len(rec_sys.products)}")
    except FileNotFoundError:
        print(f"No saved data found. Starting fresh!")
    except Exception as e:
        print(f"Error loading data: {e}")


def main():
    """Main function to run the recommendation system."""
    print("Welcome to the Recommendation System!")
    
    rec_sys = RecommendationSystem()
    load_system(rec_sys)
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-12): ").strip()
        
        if choice == "1":
            # Add user
            user_id = input("Enter user ID: ").strip()
            username = input("Enter username: ").strip()
            rec_sys.add_user(user_id, username)
        
        elif choice == "2":
            # Add product
            product_id = input("Enter product ID: ").strip()
            product_name = input("Enter product name: ").strip()
            rec_sys.add_product(product_id, product_name)
        
        elif choice == "3":
            # Record purchase
            user_id = input("Enter user ID: ").strip()
            product_id = input("Enter product ID: ").strip()
            rec_sys.add_purchase(user_id, product_id)
        
        elif choice == "4":
            # View user purchases
            user_id = input("Enter user ID: ").strip()
            rec_sys.get_user_purchases(user_id)
        
        elif choice == "5":
            # Find similar users
            user_id = input("Enter user ID: ").strip()
            n = int(input("How many similar users to show? (default 3): ").strip() or 3)
            similar = rec_sys.find_similar_users(user_id, top_n=n)
            
            if similar:
                print(f"\nMost similar users to {user_id}:")
                for similar_user_id, similarity in similar:
                    print(f"  {similar_user_id}: {similarity:.2%} similarity")
            else:
                print("No similar users found")
        
        elif choice == "6":
            # Get recommendations
            user_id = input("Enter user ID: ").strip()
            n = int(input("How many recommendations? (default 3): ").strip() or 3)
            recommendations = rec_sys.recommend_products(user_id, top_n=n)
            
            if recommendations:
                print(f"\nRecommendations for {user_id}:")
                for product_id in recommendations:
                    print(f"  - {rec_sys.products[product_id]}")
            else:
                print("No recommendations available")
        
        elif choice == "7":
            # Products bought together
            product_id = input("Enter product ID: ").strip()
            n = int(input("How many products to show? (default 3): ").strip() or 3)
            together = rec_sys.get_products_bought_together(product_id, top_n=n)
            
            if together:
                print(f"\nProducts frequently bought with {rec_sys.products.get(product_id, product_id)}:")
                for prod_id, count in together:
                    print(f"  - {rec_sys.products[prod_id]} ({count} times)")
            else:
                print("No associated products found")
        
        elif choice == "8":
            # View all users
            print("\n=== ALL USERS ===")
            if rec_sys.users:
                for user_id in rec_sys.users:
                    purchase_count = len(rec_sys.users[user_id])
                    print(f"  {user_id}: {purchase_count} purchases")
            else:
                print("No users in system")
        
        elif choice == "9":
            # View all products
            print("\n=== ALL PRODUCTS ===")
            if rec_sys.products:
                for product_id, product_name in rec_sys.products.items():
                    buyer_count = len(rec_sys.product_users[product_id])
                    print(f"  {product_id}: {product_name} ({buyer_count} buyers)")
            else:
                print("No products in system")
        
        elif choice == "10":
            # Save data
            save_system(rec_sys)
        
        elif choice == "11":
            # Load data
            load_system(rec_sys)
        
        elif choice == "12":
            # Exit
            save_system(rec_sys)
            print("\nThank you for using Recommendation System!")
            print("Goodbye! 🎯")
            break
        
        else:
            print("Invalid choice. Please enter 1-12.")


if __name__ == "__main__":
    main()
