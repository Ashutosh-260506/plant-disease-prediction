const API_URL = 'http://127.0.0.1:8000';

export const analyzePlantHealth = async (imageFile) => {
  try {
    const formData = new FormData();
    formData.append('file', imageFile);

    const response = await fetch(`${API_URL}/predict`, {
      method: 'POST',
      body: formData,
      // Do NOT set Content-Type header manually, let the browser set it with the boundary for FormData
    });

    if (!response.ok) {
      throw new Error(`Server responded with status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error in analyzePlantHealth:', error);
    throw new Error('Failed to analyze the image. Please ensure the backend is running and try again.');
  }
};
