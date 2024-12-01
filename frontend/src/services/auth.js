export const isAuthenticated = () => {
    return !!localStorage.getItem("user"); // Check if "user" exists in local storage
};

export const loginUser = (userData) => {
    localStorage.setItem("user", JSON.stringify(userData)); // Save user data in local storage
};

export const logoutUser = () => {
    localStorage.removeItem("user"); // Remove user from local storage
};
