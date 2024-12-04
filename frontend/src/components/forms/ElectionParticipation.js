import React, { useState } from "react";
import axios from "../../services/api";
import Header from "../Header";

const ElectionParticipation = () => {
  const [formData, setFormData] = useState({
    electionType: "",
  });

  const handleRadioChange = (e) => {
    const { value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      electionType: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("/forms/election-participation", {
        user_id: JSON.parse(localStorage.getItem("user")).user.id,
        interested_positions: formData.electionType,
      });
      alert(response.data.message);
    } catch (error) {
      console.error(error);
      alert("Failed to save election participation data.");
    }
  };

  return (
    <div className="container">
        <Header />
      <h2>Election Participation Form</h2>
      <form onSubmit={handleSubmit}>
        <fieldset>
          <legend>Are you interested in participating in any of the below elections?</legend>
          <label>
            <input
              type="radio"
              name="electionType"
              value="Sarpanch"
              onChange={handleRadioChange}
            />
            Sarpanch
          </label>
          <label>
            <input
              type="radio"
              name="electionType"
              value="MPTC"
              onChange={handleRadioChange}
            />
            MPTC
          </label>
          <label>
            <input
              type="radio"
              name="electionType"
              value="Municipal Ward Member"
              onChange={handleRadioChange}
            />
            Municipal Ward Member
          </label>
          <label>
            <input
              type="radio"
              name="electionType"
              value="ZPTC"
              onChange={handleRadioChange}
            />
            ZPTC
          </label>
          <label>
            <input
              type="radio"
              name="electionType"
              value="MLA"
              onChange={handleRadioChange}
            />
            MLA
          </label>
          <label>
            <input
              type="radio"
              name="electionType"
              value="MP"
              onChange={handleRadioChange}
            />
            MP
          </label>
        </fieldset>

        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default ElectionParticipation;
