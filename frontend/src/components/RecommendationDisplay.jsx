import React from "react";

const RecommendationDisplay = ({ recommendation }) => {
  console.log("Recommendation:", recommendation); // Log to verify the data structure

  return (
    <div>
      <h2>Recommendation:</h2>
      {recommendation && recommendation.length > 0 ? (
        recommendation.map((product, index) => (
          <div key={index}>
            <h3>{product.name}</h3>
            {/* Ensure augmented_info is a valid string */}
            <p>
              {typeof product.augmented_info === "string" &&
              product.augmented_info.length > 0
                ? product.augmented_info
                : "No additional information available."}
            </p>
          </div>
        ))
      ) : (
        <p>Sorry, we couldn't find products matching your interest.</p>
      )}
    </div>
  );
};

export default RecommendationDisplay;
