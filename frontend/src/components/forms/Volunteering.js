import React, { useState } from "react";
import axios from "../../services/api";
import Header from "../Header";

const Volunteering = () => {
  const [formData, setFormData] = useState({
    participationModes: [],
    feedback: "",
  });

  const handleCheckboxChange = (e) => {
    const { value, checked } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      participationModes: checked
        ? [...prevData.participationModes, value]
        : prevData.participationModes.filter((mode) => mode !== value),
    }));
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      
      const user = JSON.parse(localStorage.getItem("user"));
      console.log(user);
      const response = await axios.post("/forms/volunteering", {
        user_id: user.user.id,
        participation_methods: formData.participationModes,
        feedback: formData.feedback,
      });
      alert(response.data.message);
    } catch (error) {
      console.error(error);
      alert("Failed to save volunteering data.");
    }
  };

  return (
    <div className="container">
      <Header />
      <h2>Volunteering Form</h2>
      <form onSubmit={handleSubmit}>
        <fieldset>
          <legend>How are you planning to take part?</legend>
          <label>
            <input
              type="checkbox"
              value="On Ground Campaigns"
              onChange={handleCheckboxChange}
            />
            Taking part in On Ground Campaigns
          </label>
          <label>
            <input
              type="checkbox"
              value="Social Media"
              onChange={handleCheckboxChange}
            />
            Remotely on Social Media
          </label>
          <label>
            <input
              type="checkbox"
              value="Donating to Party"
              onChange={handleCheckboxChange}
            />
            Donating to party through party online portal
          </label>
          <label>
            <input
              type="checkbox"
              value="Finding facts through RTI"
              onChange={handleCheckboxChange}
            />
            Finding facts through RTI
          </label>
        </fieldset>

        <textarea
          name="feedback"
          placeholder="What are you liking in Aam Aadmi Party? (Optional)"
          value={formData.feedback}
          onChange={handleInputChange}
        />

        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default Volunteering;
