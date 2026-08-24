const API_URL = 'https://plant-disease-prediction-eekm.onrender.com';

export const analyzePlantHealth = async (imageFile) => {
  try {
    const formData = new FormData();
    formData.append('file', imageFile);

    const response = await fetch(`${API_URL}/predict`, {
      method: 'POST',
      body: formData,
      // Do NOT set Content-Type manually.
      // The browser adds the multipart boundary automatically.
    });

    if (!response.ok) {
      throw new Error(`Server responded with status: ${response.status}`);
    }

    const data = await response.json();
    return data;

  } catch (error) {
    console.error('Error in analyzePlantHealth:', error);

    throw new Error(
      'Failed to analyze the image. Please try again.'
    );
  }
};