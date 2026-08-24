import React, { useState, useRef } from 'react';

const UploadDropzone = ({ onPredict, isLoading }) => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [previewUrl, setPreviewUrl] = useState(null);
  const [isDragging, setIsDragging] = useState(false);
  const [error, setError] = useState(null);
  const fileInputRef = useRef(null);

  const SUPPORTED_TYPES = [
    'image/jpeg',
    'image/jpg',
    'image/png',
    'image/webp'
  ];

  const validateFile = (file) => {
    if (!file) return false;

    const isSupportedType = SUPPORTED_TYPES.includes(file.type);
    const extension = file.name.split('.').pop().toLowerCase();
    const isSupportedExtension = ['jpg', 'jpeg', 'png', 'webp'].includes(extension);

    if (!isSupportedType || !isSupportedExtension) {
      setError('Please upload a supported image format: JPG, JPEG, PNG, or WEBP.');
      return false;
    }

    setError(null);
    return true;
  };

  const handleFile = (file) => {
    if (validateFile(file)) {
      if (previewUrl) {
        URL.revokeObjectURL(previewUrl);
      }

      setSelectedFile(file);

      const url = URL.createObjectURL(file);
      setPreviewUrl(url);
    }
  };

  const onDragOver = (e) => {
    e.preventDefault();

    if (!isLoading) {
      setIsDragging(true);
    }
  };

  const onDragLeave = (e) => {
    e.preventDefault();
    setIsDragging(false);
  };

  const onDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);

    if (
      !isLoading &&
      e.dataTransfer.files &&
      e.dataTransfer.files.length > 0
    ) {
      handleFile(e.dataTransfer.files[0]);
    }
  };

  const onChange = (e) => {
    if (
      !isLoading &&
      e.target.files &&
      e.target.files.length > 0
    ) {
      handleFile(e.target.files[0]);
    }
  };

  const handleRemove = () => {
    if (isLoading) return;

    setSelectedFile(null);

    if (previewUrl) {
      URL.revokeObjectURL(previewUrl);
    }

    setPreviewUrl(null);
    setError(null);

    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  const formatFileSize = (bytes) => {
    if (bytes === 0) return '0 Bytes';

    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));

    return (
      parseFloat((bytes / Math.pow(k, i)).toFixed(2)) +
      ' ' +
      sizes[i]
    );
  };

  return (
    <div
      style={{
        width: '100%',
        maxWidth: '600px',
        margin: '0 auto'
      }}
    >
      {!selectedFile ? (
        <div
          className={`dropzone ${isDragging ? 'dragging' : ''}`}
          onDragOver={onDragOver}
          onDragLeave={onDragLeave}
          onDrop={onDrop}
          onClick={() =>
            !isLoading && fileInputRef.current?.click()
          }
          style={{
            opacity: isLoading ? 0.6 : 1,
            cursor: isLoading ? 'default' : 'pointer'
          }}
        >
          <input
            type="file"
            ref={fileInputRef}
            onChange={onChange}
            accept=".jpg,.jpeg,.png,.webp"
            style={{ display: 'none' }}
            disabled={isLoading}
          />

          <div
            style={{
              marginBottom: '16px',
              display: 'flex',
              justifyContent: 'center'
            }}
          >
            <div
              style={{
                width: '80px',
                height: '80px',
                borderRadius: '50%',
                background: 'rgba(185, 246, 196, 0.05)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                border: '1px solid rgba(185, 246, 196, 0.1)'
              }}
            >
              <svg
                width="40"
                height="40"
                viewBox="0 0 24 24"
                fill="none"
                stroke="var(--accent)"
                strokeWidth="1.5"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z" />
                <path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12" />
              </svg>
            </div>
          </div>

          <h3
            style={{
              fontSize: '1.25rem',
              color: 'var(--text-primary)',
              marginBottom: '8px',
              fontWeight: 500
            }}
          >
            Drop your plant image here
          </h3>

          <p
            style={{
              color: 'var(--text-secondary)',
              marginBottom: '16px',
              fontSize: '0.95rem'
            }}
          >
            or click to browse
          </p>

          <p
            style={{
              color: 'var(--text-muted)',
              fontSize: '0.85rem'
            }}
          >
            JPG • JPEG • PNG • WEBP
          </p>

          {error && (
            <div
              style={{
                marginTop: '16px',
                color: 'var(--danger)',
                fontSize: '0.9rem',
                background: 'rgba(255, 143, 143, 0.1)',
                padding: '8px 16px',
                borderRadius: '12px'
              }}
            >
              {error}
            </div>
          )}
        </div>
      ) : (
        <div
          style={{
            background: 'var(--glass-bg)',
            backdropFilter: 'var(--glass-blur)',
            border: '1px solid var(--border)',
            borderRadius: '24px',
            padding: '24px',
            display: 'flex',
            flexDirection: 'column',
            gap: '24px',
            animation: 'fadeIn 0.3s ease-out'
          }}
        >
          <div
            style={{
              position: 'relative',
              width: '100%',
              height: '320px',
              borderRadius: '16px',
              overflow: 'hidden',
              border: '1px solid rgba(255, 255, 255, 0.1)'
            }}
          >
            <img
              src={previewUrl}
              alt="Plant preview"
              style={{
                width: '100%',
                height: '100%',
                objectFit: 'cover',
                opacity: isLoading ? 0.65 : 1,
                transition: 'opacity 0.3s'
              }}
            />

            {isLoading && (
              <div
                className="analysis-overlay"
                style={{
                  position: 'absolute',
                  top: 0,
                  left: 0,
                  right: 0,
                  bottom: 0,
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'center',
                  justifyContent: 'center',
                  background: 'rgba(7, 16, 11, 0.68)',
                  color: 'var(--accent)',
                  overflow: 'hidden'
                }}
              >
                <div className="scan-line"></div>

                <div
                  className="spinner"
                  style={{
                    marginBottom: '14px'
                  }}
                ></div>

                <p
                  style={{
                    fontWeight: 600,
                    marginBottom: '6px'
                  }}
                >
                  Analyzing plant...
                </p>

                <p
                  style={{
                    color: 'var(--text-secondary)',
                    fontSize: '0.85rem'
                  }}
                >
                  AI is examining the leaf
                </p>
              </div>
            )}
          </div>

          <div
            style={{
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center'
            }}
          >
            <div
              style={{
                overflow: 'hidden',
                paddingRight: '16px'
              }}
            >
              <p
                style={{
                  color: 'var(--text-primary)',
                  fontWeight: 500,
                  whiteSpace: 'nowrap',
                  overflow: 'hidden',
                  textOverflow: 'ellipsis'
                }}
              >
                {selectedFile.name}
              </p>

              <p
                style={{
                  color: 'var(--text-muted)',
                  fontSize: '0.85rem'
                }}
              >
                {formatFileSize(selectedFile.size)}
              </p>
            </div>

            <button
              onClick={handleRemove}
              className="btn-secondary"
              disabled={isLoading}
              style={{
                opacity: isLoading ? 0.5 : 1,
                cursor: isLoading ? 'not-allowed' : 'pointer'
              }}
            >
              Change Image
            </button>
          </div>

          <button
            onClick={() =>
              onPredict && onPredict(selectedFile)
            }
            className="btn-primary"
            disabled={isLoading}
          >
            {isLoading ? (
              <>
                <div className="spinner spinner-small"></div>
                Processing...
              </>
            ) : (
              <>
                <svg
                  width="20"
                  height="20"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <circle cx="12" cy="12" r="10" />
                  <path d="M12 16v-4" />
                  <path d="M12 8h.01" />
                </svg>

                Analyze Plant Health
              </>
            )}
          </button>
        </div>
      )}

      <style>{`
        @keyframes fadeIn {
          from {
            opacity: 0;
            transform: translateY(10px);
          }

          to {
            opacity: 1;
            transform: translateY(0);
          }
        }

        .spinner {
          width: 32px;
          height: 32px;
          border: 3px solid rgba(185, 246, 196, 0.3);
          border-radius: 50%;
          border-top-color: var(--accent);
          animation: spin 1s ease-in-out infinite;
        }

        .spinner-small {
          width: 20px;
          height: 20px;
          border-width: 2px;
        }

        @keyframes spin {
          to {
            transform: rotate(360deg);
          }
        }

        .scan-line {
          position: absolute;
          left: 0;
          right: 0;
          height: 2px;
          background: var(--accent);
          box-shadow: 0 0 18px rgba(185, 246, 196, 0.8);
          animation: scan 2s ease-in-out infinite;
        }

        @keyframes scan {
          0%,
          100% {
            top: 10%;
            opacity: 0.3;
          }

          50% {
            top: 90%;
            opacity: 1;
          }
        }
      `}</style>
    </div>
  );
};

export default UploadDropzone;