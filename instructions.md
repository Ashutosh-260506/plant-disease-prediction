# P3 Plant Disease Prediction — Project Instructions & Constraints

## 1. Project Goal

Build a production-style Plant Disease Prediction application using:

- Fine-tuned EfficientNetB0
- FastAPI backend
- React + Vite frontend
- Grad-CAM explainability
- Docker
- Clean documentation and portfolio-quality presentation

The final application should allow a user to upload a plant leaf image and receive:
1. Predicted disease
2. Prediction confidence
3. Grad-CAM visual explanation

The project should demonstrate both Deep Learning and software-engineering/deployment skills.

## 2. Existing ML Model

The finalized model is a fine-tuned EfficientNetB0.

Current known results:
- Validation accuracy: approximately 97%
- Number of classes: 38
- Input size: 224 × 224 × 3
- Architecture: preprocessing → EfficientNetB0 → GlobalAveragePooling2D → Dropout → Dense(38)

Model:
`backend/model/plant_disease_model.keras`

Class names:
`backend/model/class_names.json`

### Critical constraints

DO NOT retrain, replace, quantize, prune, or otherwise alter the trained model unless explicitly requested.

Do not change class ordering in `class_names.json`.

Always load class names from `class_names.json`; do not hard-code all 38 classes.

## 3. Inference Constraints

The existing inference pipeline is:

Image → RGB → resize to 224×224 → batch dimension → EfficientNetB0 → 38-class prediction.

Do not add manual normalization that conflicts with the saved Keras EfficientNet preprocessing.

Preserve the existing prediction behavior.

## 4. FastAPI Backend

Backend location:
`backend/`

Existing endpoints:

### GET `/`
Health check.

### GET `/model-info`
Returns model information such as architecture and class count.

### POST `/predict`

Request:
- `multipart/form-data`
- field name: `file`

Current response contract:

```json
{
  "disease": "Grape___Black_rot",
  "confidence": 0.999998,
  "gradcam": "<base64 JPEG string>"
}
```

### Critical API constraint

Do NOT change the `/predict` request or response contract unless explicitly requested.

The frontend must adapt to the existing API.

## 5. CORS

React development server will normally use:
`http://localhost:5173`

FastAPI:
`http://127.0.0.1:8000`

If needed, add only the minimum `CORSMiddleware` configuration required for local development.

Do not broadly allow every origin in the final production configuration.

## 6. Grad-CAM

Grad-CAM is already implemented in:

- `backend/app/gradcam.py`
- `backend/app/visualization.py`

It uses EfficientNetB0's `top_conv` layer.

Feature map:
`7 × 7 × 1280`

Heatmap:
`7 × 7`

### Grad-CAM constraints

Do not:
- Retrain the model because of Grad-CAM
- Change the target convolutional layer without a clear reason
- Call Grad-CAM a segmentation algorithm
- Claim every red pixel is a disease lesion
- Claim Grad-CAM proves causal reasoning

Correct description:

> Grad-CAM provides a visual explanation of image regions that contributed strongly to the model's prediction.

Activation outside the leaf can occur because the feature map is coarse and upsampled. Background/contextual bias may also exist. Do not hide these limitations.

## 7. React Frontend

Location:
`frontend/`

Use:
- React
- Vite
- JavaScript
- Plain CSS

Do NOT use TypeScript unless explicitly requested.

Do NOT add unnecessary UI frameworks or libraries.

Keep code modular and understandable.

Recommended structure:

```text
frontend/
├── src/
│   ├── components/
│   ├── services/
│   ├── App.jsx
│   ├── main.jsx
│   └── index.css
├── package.json
└── ...
```

## 8. Frontend Requirements

### Upload
- Drag-and-drop
- File picker
- Image preview
- Clear/remove image

### Prediction
- Predict button
- Loading state
- Error state
- Prevent duplicate requests while processing

### Results
Display:
- Disease name
- Confidence percentage
- Original image
- Grad-CAM visualization

### UX
The interface should be:
- Responsive
- Modern
- Professional
- Portfolio-quality
- Accessible
- Easy to understand

Avoid excessive animation that hurts usability.

## 9. API Integration

Call:

`POST http://127.0.0.1:8000/predict`

Use `FormData` with field:
`file`

Do not manually set `Content-Type` for `FormData`; the browser must set the multipart boundary.

Grad-CAM should be displayed from:

`data:image/jpeg;base64,<response.gradcam>`

Do not create unnecessary permanent image files.

## 10. Backend Safety

Do not make broad changes to:
- `model.py`
- `preprocessing.py`
- `gradcam.py`
- `visualization.py`

unless explicitly required.

Before modifying existing backend logic:
1. Understand it.
2. Explain why the change is necessary.
3. Make the smallest possible change.
4. Retest `/predict`.

The backend is currently working.

## 11. Docker

Dockerization comes AFTER:
1. Backend works
2. Grad-CAM works
3. React works
4. React ↔ FastAPI integration works
5. Local end-to-end testing succeeds

Do not start Docker prematurely.

Keep Docker configuration simple and reproducible.

## 12. Testing

Test each component independently.

### Model
- Model loads
- 38 classes load
- Prediction works

### FastAPI
- `/`
- `/model-info`
- `/predict`

### Grad-CAM
- Heatmap generated
- Heatmap shape is 7×7
- Overlay generated

### Frontend
- Upload
- Preview
- API request
- Loading
- Prediction
- Confidence
- Grad-CAM
- Error handling

### End-to-end

Verify:

`Browser → React → FastAPI → EfficientNet → Grad-CAM → React`

## 13. Error Handling

Gracefully handle:
- No image
- Invalid file type
- Very large files
- Backend unavailable
- API errors
- Invalid/empty API responses
- Image processing errors

Do not expose Python stack traces to normal users.

## 14. Code Quality

Prioritize:
- Clear naming
- Small functions
- Separation of concerns
- Reusable components
- Minimal duplication
- Readability
- Simple architecture

Avoid:
- Unnecessary abstractions
- Huge files
- Duplicate logic
- Hard-coded values where configuration is appropriate
- Dead code
- Debug prints in production

Use comments only when they explain genuinely non-obvious logic.

## 15. Learning Requirement

The project owner is learning the technologies.

When implementing a new component:
1. Explain what it does.
2. Explain important concepts.
3. Keep the implementation understandable.
4. Explain major architectural decisions.
5. Prefer simple solutions over clever ones.

AI-generated code must not become a black box.

The developer should understand:
- React components
- State and props
- API calls
- FormData
- FastAPI endpoints
- Base64 images
- Grad-CAM
- Docker basics
- Overall architecture

## 16. AI Agent Rules

Before modifying files:
1. Inspect relevant existing files.
2. Understand dependencies.
3. Avoid unrelated changes.
4. Present a plan for major changes.

During implementation:
- Make incremental changes.
- Test after meaningful changes.
- Report what changed.
- Report commands used for testing.
- Distinguish warnings from actual failures.

Never claim something works unless it was tested.

Do not overwrite working code unnecessarily.

## 17. Do Not Change Without Permission

Do not independently:
- Retrain the model
- Change model architecture
- Change class labels
- Change preprocessing
- Change API contract
- Remove Grad-CAM
- Replace FastAPI
- Replace React
- Add a database
- Add authentication
- Add cloud infrastructure
- Add unnecessary third-party services

These require explicit approval.

## 18. Target Architecture

```text
P3-Plant-Disease-Prediction/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── model.py
│   │   ├── preprocessing.py
│   │   ├── gradcam.py
│   │   └── visualization.py
│   │
│   ├── model/
│   │   ├── plant_disease_model.keras
│   │   └── class_names.json
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   └── ...
│
├── notebooks/
├── Test_img/
├── Dockerfile
├── .gitignore
├── instructions.md
└── README.md
```

The structure may evolve only when there is a clear reason.

## 19. Final Features

The finished project should demonstrate:

- Deep Learning
- Transfer Learning
- EfficientNetB0
- Multi-class image classification
- Model evaluation
- FastAPI
- REST API
- React
- API integration
- Grad-CAM
- Explainable AI
- Docker
- Git/GitHub
- Production-oriented structure

## 20. Resume Positioning

Suggested project title:

**Plant Disease Detection & Explainable AI System**

Possible description:

> Developed a 38-class plant disease detection system using a fine-tuned EfficientNetB0 model achieving approximately 97% validation accuracy; deployed inference through FastAPI, integrated Grad-CAM for visual model explanations, and built a React frontend with Docker-ready architecture.

Do not claim production deployment, real-world reliability, or perfect explainability unless actually demonstrated.

## 21. Documentation

Final `README.md` should include:
1. Overview
2. Problem statement
3. Features
4. Dataset
5. Model architecture
6. Training/fine-tuning
7. Evaluation metrics
8. Classification report/confusion matrix where appropriate
9. Grad-CAM
10. Backend architecture
11. API documentation
12. Frontend
13. Installation
14. Local development
15. Docker
16. Screenshots
17. Limitations
18. Future improvements
19. Architecture
20. Author information

Documentation must accurately reflect the implemented system.

## 22. ML Limitations

High PlantVillage-style validation accuracy does not guarantee equivalent real-world performance.

Real-world images can differ in:
- Lighting
- Background
- Camera quality
- Leaf orientation
- Disease severity
- Multiple leaves
- Multiple diseases
- Occlusion
- Image composition

Mention domain shift and possible background/context bias where appropriate.

## 23. Current Status

Completed:
- EfficientNetB0 training/fine-tuning
- Model evaluation
- Model saving/loading
- FastAPI
- Model inference API
- Grad-CAM
- Grad-CAM visualization
- FastAPI + Grad-CAM integration
- `/predict` successfully tested

Current task:
**React frontend**

Future:
- React ↔ FastAPI integration testing
- UI polish
- Dockerization
- Final testing
- README
- GitHub cleanup
- Resume/LinkedIn presentation

## 24. Golden Rule

### Preserve what already works.

Before changing anything, ask:

> Is this change necessary for the current requirement?

If not, do not change it.

Build incrementally, test frequently, keep the architecture understandable, and prioritize correctness over unnecessary complexity.


## 25. Model Integrity & Reproducibility

The trained model is a finalized project artifact.

AI agents MUST NOT:
- Retrain the model
- Change the model architecture
- Change EfficientNetB0 weights
- Change the model's input size
- Add/remove preprocessing layers
- Change class ordering
- Replace the `.keras` model
- Change TensorFlow/Keras behavior merely for "optimization"
- Recreate the model from scratch when the saved artifact can be loaded

Any proposed model-side change requires explicit approval.

Preserve the inference behavior that has already been validated.

Dependency upgrades must not be performed casually. If a dependency must change, verify that model loading, prediction, Grad-CAM, and the API still work afterward.

## 26. Protect the Working Grad-CAM Implementation

The current Grad-CAM implementation is working and has already been tested through the FastAPI `/predict` endpoint.

Do not refactor or rewrite `gradcam.py` or `visualization.py` simply for style.

Before changing either file:
1. Explain the exact reason.
2. Explain the expected effect.
3. Make the smallest possible change.
4. Test Grad-CAM independently.
5. Test `/predict` again.

The nested EfficientNet architecture and `top_conv` graph connectivity are important implementation details. Do not replace the working graph construction with a different approach without verification.

## 27. Data and Dataset Integrity

Do not modify the training dataset as part of frontend/backend development.

Do not:
- Rename class labels
- Reorder labels
- Add synthetic classes
- Delete dataset classes
- Change the training/validation split
- Retrain using arbitrary real-world images

Real-world test images may be used for inference testing, but their results must not be presented as validation metrics.

Never mix test images into reported validation metrics.

## 28. Security and Privacy

Never expose:
- Model filesystem paths
- Local Windows usernames/paths
- Environment variables
- API keys
- Passwords
- Tokens
- Credentials
- Internal stack traces

Do not commit secrets to GitHub.

Use environment variables for future secrets/configuration.

Do not create unnecessary telemetry or collect user-uploaded images without explicit need.

Uploaded images should be processed only as required for inference and should not be permanently stored unless explicitly requested.

## 29. Git and `.gitignore`

The project must not commit unnecessary local or generated files.

`.gitignore` should cover at minimum:

```text
venv/
.venv/
__pycache__/
*.pyc
.env
.env.*
.vscode/
.idea/
*.log
.DS_Store
node_modules/
dist/
build/
```

Also exclude temporary/generated test artifacts where appropriate, such as temporary Grad-CAM output files.

Do not commit:
- Virtual environments
- Cache files
- Secrets
- Temporary logs
- Unnecessary generated images
- Large unrelated files

The trained `.keras` model should only be committed if the repository strategy intentionally supports its size and distribution. If it is too large for normal GitHub usage, document the chosen model-storage approach instead of silently committing it.

## 30. No Unnecessary Services

Do not add the following unless explicitly requested:

- Database
- Authentication
- User accounts
- Cloud storage
- Payment system
- Message queue
- Redis
- Kubernetes
- Microservices
- External AI APIs
- Additional ML models
- Analytics/tracking

The application should remain a focused plant-disease AI system.

## 31. Frontend Must Not Access the Model Directly

The React application must NEVER load or contain:

`plant_disease_model.keras`

Inference must always happen through FastAPI:

```text
React
  ↓
FastAPI /predict
  ↓
EfficientNetB0
  ↓
Prediction + Grad-CAM
  ↓
React
```

The model remains a backend-side artifact.

## 32. API Security and Validation

The backend should validate uploaded files where practical.

At minimum:
- Accept normal image formats
- Reject obviously invalid uploads
- Handle corrupted images gracefully
- Avoid returning internal Python exceptions to users
- Avoid unnecessary permanent storage of uploads

Do not make the API unnecessarily complex.

## 33. Configuration

Do not hard-code secrets.

For local non-secret configuration, hard-coded values are acceptable when they are simple and stable, but use environment variables when configuration needs to differ between development and production.

If an environment variable is introduced:
1. Document it.
2. Add it to an example configuration if appropriate.
3. Never commit the real secret value.

## 34. AI Agent Change Policy

For every meaningful change, the agent should report:

1. Files changed
2. What changed
3. Why it changed
4. Commands/tests executed
5. Test result
6. Any warnings that remain

For potentially destructive operations, request approval first.

Do not delete or overwrite existing working files without a clear reason.

Do not install large numbers of packages without explaining why each is needed.

## 35. Dependency Discipline

Prefer the smallest reasonable dependency set.

Before adding a package, ask:

> Is this dependency necessary for the current requirement?

Prefer built-in browser APIs, Python standard-library functionality, or existing project dependencies when they are sufficient.

Do not install alternative packages simply because an existing package has a warning if the existing implementation still works.

When a package is required:
- Install it in the project environment
- Update `requirements.txt` or `package.json`
- Verify the application afterward

## 36. No Unsupported Claims

The application and README must not claim:

- 100% accuracy
- Perfect diagnosis
- Medical-grade diagnosis
- Guaranteed agricultural recommendations
- Exact disease localization
- Perfect explainability
- Production readiness unless actually deployed/tested

Use accurate wording such as:

> AI-assisted plant disease prediction

and:

> Grad-CAM visual explanation of regions contributing to the prediction.

## 37. Real-World Performance

The reported ~97% validation accuracy comes from the project's validation dataset.

Do not present it as guaranteed real-world accuracy.

If real-world images are tested, report them separately as qualitative examples unless a properly designed independent test set is created.

Potential domain-shift factors include:
- Background
- Lighting
- Camera/device
- Leaf orientation
- Disease severity
- Image quality
- Multiple leaves
- Occlusion

These limitations should appear in the final README.

## 38. Browser Testing

When the frontend is implemented, test the actual browser workflow:

1. Start FastAPI.
2. Start React.
3. Open the frontend.
4. Upload a valid image.
5. Confirm preview.
6. Click Predict.
7. Confirm loading state.
8. Confirm disease.
9. Confirm confidence.
10. Confirm Grad-CAM image.
11. Test an invalid upload.
12. Test backend-unavailable behavior.

Do not claim frontend integration works based only on static code inspection.

## 39. Production vs Development

Clearly distinguish:
- Local development
- Docker/local production-like testing
- Actual deployment

Do not call a local development server a production deployment.

If Docker is added, verify the containerized application independently instead of assuming that working locally means Docker works.

## 40. Final Quality Gate

Before considering the project complete, verify:

### ML
- [ ] Saved model loads
- [ ] 38 classes load
- [ ] Prediction works
- [ ] Reported metrics are reproducible from documented evaluation

### Grad-CAM
- [ ] Heatmap generated
- [ ] Heatmap shape is 7×7
- [ ] Overlay generated
- [ ] Explanation wording is technically accurate

### Backend
- [ ] FastAPI starts
- [ ] `/` works
- [ ] `/model-info` works
- [ ] `/predict` works
- [ ] CORS works for the frontend
- [ ] Invalid input is handled

### Frontend
- [ ] React starts
- [ ] Upload works
- [ ] Preview works
- [ ] API request works
- [ ] Loading works
- [ ] Error handling works
- [ ] Disease displayed
- [ ] Confidence displayed
- [ ] Grad-CAM displayed
- [ ] Responsive layout works

### Security
- [ ] No secrets committed
- [ ] No local paths exposed
- [ ] No unnecessary uploaded-image storage
- [ ] `.gitignore` is appropriate

### Docker
- [ ] Docker build succeeds
- [ ] Container starts
- [ ] Backend inference works in the intended Docker setup
- [ ] Frontend/backend communication works in the intended setup

### Documentation
- [ ] README matches actual implementation
- [ ] Installation instructions tested
- [ ] API documented
- [ ] Architecture documented
- [ ] Limitations documented
- [ ] Screenshots included where useful

Only after these checks should the project be described as complete.
