import React, { useState } from 'react';
import UploadDropzone from './components/UploadDropzone';
import ResultCard from './components/ResultCard';
import { analyzePlantHealth } from './services/api';

function App() {
  const [isLoading, setIsLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [originalImage, setOriginalImage] = useState(null);

  const handlePredict = async (file) => {
    setIsLoading(true);
    setResult(null);
    setError(null);

    const imageUrl = URL.createObjectURL(file);
    setOriginalImage(imageUrl);

    try {
      const data = await analyzePlantHealth(file);
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app-container">
      <header style={{ padding: '24px', borderBottom: 'var(--glass-border)' }}>
        <h2 style={{ fontSize: '1.2rem', fontWeight: 600 }}>PlantLens AI</h2>
      </header>

      <main style={{ flex: 1, padding: '48px 24px', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <div style={{ textAlign: 'center', marginBottom: '48px' }}>
          <span style={{
            display: 'inline-block',
            padding: '4px 12px',
            borderRadius: '999px',
            border: 'var(--glass-border)',
            background: 'rgba(20, 30, 23, 0.4)',
            color: 'var(--accent)',
            fontSize: '0.8rem',
            marginBottom: '16px',
            letterSpacing: '0.05em',
            fontWeight: 500
          }}>
            ◉ AI POWERED PLANT HEALTH
          </span>
          <h1 style={{ fontSize: 'clamp(2.5rem, 5vw, 4rem)', lineHeight: 1.1, marginBottom: '16px', letterSpacing: '-0.02em' }}>
            See the health<br />of your plants.
          </h1>
          <p style={{ color: 'var(--text-secondary)', maxWidth: '500px', margin: '0 auto', fontSize: '1.1rem' }}>
            Upload a plant image and let AI analyze its health.
          </p>
        </div>

        {!result ? (
          <>
            <UploadDropzone onPredict={handlePredict} isLoading={isLoading} />
            {error && (
              <div style={{ marginTop: '24px', padding: '16px', background: 'rgba(255, 143, 143, 0.1)', color: 'var(--danger)', borderRadius: '12px', border: '1px solid rgba(255, 143, 143, 0.2)', maxWidth: '600px', width: '100%', textAlign: 'center' }}>
                {error}
              </div>
            )}
          </>
        ) : (
          <ResultCard
            result={result}
            originalImage={originalImage}
            onReset={() => {
              setResult(null);
              setOriginalImage(null);
              setError(null);
            }}
          />
        )}
      </main>
    </div>
  );
}

export default App;
