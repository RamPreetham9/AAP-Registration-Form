import React, { useState } from "react";
import axios from "../../services/api";
import { useNavigate } from "react-router-dom";

const Wizard = () => {
  const [currentStep, setCurrentStep] = useState(1);
  const [formData, setFormData] = useState({
    voter_district: "",
    voter_assembly: "",
    voter_parliament: "",
    voter_city: "",
    voter_mandal: "",
    voter_ward: "",
    elections: [],
    participation: [],
    likes: "",
  });

  const navigate = useNavigate();

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleCheckboxChange = (key, value) => {
    setFormData((prevState) => {
      const updatedList = prevState[key].includes(value)
        ? prevState[key].filter((item) => item !== value)
        : [...prevState[key], value];
      return { ...prevState, [key]: updatedList };
    });
  };

  const handleNext = () => {
    if (currentStep < 3) {
      setCurrentStep(currentStep + 1);
    } else {
      handleSubmit();
    }
  };

  const handlePrev = () => {
    if (currentStep > 1) {
      setCurrentStep(currentStep - 1);
    }
  };

  const handleSubmit = async () => {
    const payload = {
      user: {
        user_id: JSON.parse(localStorage.getItem("user")).user_id
      },
      p1: {
        voter_district: formData.voter_district,
        voter_assembly: formData.voter_assembly,
        voter_parliament: formData.voter_parliament,
        voter_city: formData.voter_city,
        voter_mandal: formData.voter_mandal,
        voter_ward: formData.voter_ward,
      },
      p2: {
        elections: formData.elections,
      },
      p3: {
        participation: formData.participation,
        likes: formData.likes,
      },
    };

    try {
      const response = await axios.post("/auth/complete-registration", payload);
      alert(response.data.message);
      navigate("/");
    } catch (error) {
      console.error(error);
      alert("Failed to complete registration. Please try again.");
    }
  };

  return (
    <div className="container">
      <h2>Step {currentStep} of 3</h2>

      {currentStep === 1 && (
        <div>
          <h3>Location Details</h3>
          <select
            name="voter_district"
            value={formData.voter_district}
            onChange={handleInputChange}
            required
          >
            <option value="">Select District</option>
            <option value="Anantapur">Anantapur</option>
            <option value="Chittoor">Chittoor</option>
            {/* Add more options */}
          </select>

          <select
            name="voter_assembly"
            value={formData.voter_assembly}
            onChange={handleInputChange}
          >
            <option value="">Select Assembly</option>
            <option value="Anantapur Urban">Anantapur Urban</option>
            <option value="Tirupati">Tirupati</option>
            {/* Add more options */}
          </select>

          <select
            name="voter_parliament"
            value={formData.voter_parliament}
            onChange={handleInputChange}
          >
            <option value="">Select Parliament</option>
            <option value="Anantapur">Anantapur</option>
            <option value="Tirupati">Tirupati</option>
            {/* Add more options */}
          </select>

          <select
            name="voter_city"
            value={formData.voter_city}
            onChange={handleInputChange}
          >
            <option value="">Select City</option>
            <option value="City 1">City 1</option>
            <option value="City 2">City 2</option>
            {/* Add more options */}
          </select>

          <select
            name="voter_mandal"
            value={formData.voter_mandal}
            onChange={handleInputChange}
          >
            <option value="">Select Mandal</option>
            <option value="Mandal 1">Mandal 1</option>
            <option value="Mandal 2">Mandal 2</option>
            {/* Add more options */}
          </select>

          <input
            type="text"
            name="voter_ward"
            placeholder="Ward No."
            value={formData.voter_ward}
            onChange={handleInputChange}
          />
        </div>
      )}

      {currentStep === 2 && (
        <div>
          <h3>Election Participation</h3>
          <p>Select the elections you're interested in:</p>
          {[
            "Sarpanch",
            "MPTC",
            "Municipal Ward Member",
            "ZPTC",
            "MLA",
            "MP",
          ].map((option) => (
            <label key={option}>
              <input
                type="checkbox"
                value={option}
                checked={formData.elections.includes(option)}
                onChange={() => handleCheckboxChange("elections", option)}
              />
              {option}
            </label>
          ))}
        </div>
      )}

      {currentStep === 3 && (
        <div>
          <h3>Volunteering</h3>
          <p>How do you plan to contribute?</p>
          {[
            "Taking part in On Ground Campaigns",
            "Remotely on Social Media",
            "Donating to party through party online portal",
            "Finding facts through RTI",
          ].map((option) => (
            <label key={option}>
              <input
                type="checkbox"
                value={option}
                checked={formData.participation.includes(option)}
                onChange={() => handleCheckboxChange("participation", option)}
              />
              {option}
            </label>
          ))}

          <textarea
            name="likes"
            placeholder="What do you like about AAP? (Optional)"
            value={formData.likes}
            onChange={handleInputChange}
          />
        </div>
      )}

      <div className="navigation-buttons">
        {currentStep > 1 && <button onClick={handlePrev}>Previous</button>}
        <button onClick={handleNext}>
          {currentStep < 3 ? "Next" : "Submit"}
        </button>
      </div>
    </div>
  );
};

export default Wizard;
