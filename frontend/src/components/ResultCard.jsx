function formatDiseaseName(disease) {
    if (!disease) return "Unknown";

    return disease
        .replace(/___/g, " — ")
        .replace(/_/g, " ");
}

function getConfidenceLevel(confidence) {
    if (confidence >= 90) {
        return "High model confidence";
    }

    if (confidence >= 70) {
        return "Moderate model confidence";
    }

    return "Lower model confidence";
}

function ResultCard({ result, originalImage, onReset }) {
    const confidence = Math.max(
        0,
        Math.min(100, result.confidence * 100)
    );

    const diseaseName = formatDiseaseName(result.disease);
    const confidenceLevel = getConfidenceLevel(confidence);

    const gradcamImage = result.gradcam
        ? `data:image/jpeg;base64,${result.gradcam}`
        : null;

    return (
        <div className="result-container">

            {/* Result Header */}
            <div className="result-header">

                <span className="result-badge">
                    ◉ PLANT ANALYSIS COMPLETE
                </span>

                <h2>
                    {diseaseName}
                </h2>

                <p>
                    AI-powered prediction based on the uploaded plant image.
                </p>

            </div>


            {/* Confidence */}
            <div className="confidence-card">

                <div className="confidence-top">

                    <div>
                        <span>Model Confidence</span>

                        <small
                            style={{
                                display: "block",
                                color: "var(--text-muted)",
                                marginTop: "4px"
                            }}
                        >
                            {confidenceLevel}
                        </small>
                    </div>

                    <strong>
                        {confidence.toFixed(2)}%
                    </strong>

                </div>

                <div className="confidence-track">

                    <div
                        className="confidence-fill"
                        style={{
                            width: `${confidence}%`
                        }}
                    />

                </div>

            </div>


            {/* Image Comparison */}
            <div className="image-grid">

                {/* Original Image */}
                <div className="image-card">

                    <div className="image-label">
                        Original Image
                    </div>

                    {originalImage ? (
                        <img
                            src={originalImage}
                            alt="Uploaded plant"
                        />
                    ) : (
                        <div className="image-placeholder">
                            Original image unavailable
                        </div>
                    )}

                </div>


                {/* Grad-CAM */}
                <div className="image-card">

                    <div className="image-label">
                        AI Focus
                    </div>

                    {gradcamImage ? (
                        <img
                            src={gradcamImage}
                            alt="Grad-CAM visualization showing regions influencing the prediction"
                        />
                    ) : (
                        <div className="image-placeholder">
                            AI visualization unavailable
                        </div>
                    )}

                </div>

            </div>


            {/* Grad-CAM Explanation */}
            <div className="gradcam-info">

                <strong>
                    How AI Focus works
                </strong>

                <p>
                    AI Focus highlights the regions that contributed most
                    strongly to the model's prediction.
                </p>

                <p
                    style={{
                        marginTop: "8px",
                        color: "var(--text-muted)",
                        fontSize: "0.82rem"
                    }}
                >
                    Warmer colors indicate regions that had a stronger
                    influence on the prediction.
                </p>

            </div>


            {/* Disclaimer */}
            <div
                className="result-disclaimer"
                style={{
                    marginTop: "16px",
                    padding: "14px 16px",
                    borderRadius: "12px",
                    border: "1px solid rgba(185, 246, 196, 0.08)",
                    background: "rgba(185, 246, 196, 0.025)",
                    color: "var(--text-muted)",
                    fontSize: "0.78rem",
                    lineHeight: "1.5"
                }}
            >
                <strong
                    style={{
                        color: "var(--text-secondary)"
                    }}
                >
                    Note:
                </strong>{" "}
                This prediction is AI-generated and should be used as a
                supporting tool rather than a substitute for expert
                agricultural diagnosis.
            </div>


            {/* Reset */}
            <button
                className="btn-secondary"
                onClick={onReset}
                style={{
                    marginTop: "20px",
                    width: "100%"
                }}
            >
                Analyze Another Image
            </button>

        </div>
    );
}

export default ResultCard;