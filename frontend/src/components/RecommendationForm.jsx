import React, { useState } from "react";
import axios from "axios";

const RecommendationForm = () => {
  const [userInterest, setUserInterest] = useState("");
  const [recommendation, setRecommendation] = useState([]);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://localhost:8000/api/recommend/",
        {
          user_interest: userInterest,
        }
      );
      setRecommendation(response.data.recommendation); // This should be an array
      setError("");
    } catch (err) {
      setError("Something went wrong, please try again.");
    }
  };

  return (
    <div>
      <h2>BakedBot - Product Recommendations</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter your interest"
          value={userInterest}
          onChange={(e) => setUserInterest(e.target.value)}
        />
        <button type="submit">Get Recommendation</button>
      </form>

      {/* Rendering recommendation array */}
      {recommendation.length > 0 ? (
        recommendation.map((product, index) => (
          <div key={index}>
            <h3>{product.name}</h3>
            <p>{product.augmented_info}</p>
          </div>
        ))
      ) : (
        <p>No recommendations yet. Please enter an interest!</p>
      )}

      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
};

export default RecommendationForm;
