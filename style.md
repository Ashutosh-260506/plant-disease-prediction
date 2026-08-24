# P3 Plant Disease Prediction — UI Style Guide

This document defines the visual direction for the frontend.

The uploaded reference image is the primary visual inspiration. Recreate its **design language and user experience**, not its branding, exact text, or exact layout.

---

## 1. Overall Design Direction

Create a premium, modern AI-powered plant-health interface.

The visual feeling should be:

- Premium
- Minimal
- Natural
- Modern
- Sophisticated
- Trustworthy
- AI-focused
- Clean rather than overly decorative

The application should feel like a polished startup/product website rather than a college-project dashboard.

Reference visual characteristics:

- Dark cinematic background
- Large rounded main container
- High-quality plant imagery
- Strong white typography
- Green/nature-inspired accents
- Glassmorphism cards
- Soft gradients
- Subtle borders
- Rounded corners
- Large whitespace
- Minimal navigation
- Strong visual hierarchy

Do NOT copy the reference site's branding, logo, text, or exact visual assets.

---

## 2. Color System

Use a nature-inspired dark palette.

Suggested CSS variables:

```css
:root {
  --bg-primary: #07100b;
  --bg-secondary: #0d1711;
  --surface: rgba(20, 29, 22, 0.72);
  --surface-strong: rgba(18, 27, 20, 0.9);
  --border: rgba(255, 255, 255, 0.12);

  --text-primary: #f5f7f3;
  --text-secondary: rgba(245, 247, 243, 0.68);
  --text-muted: rgba(245, 247, 243, 0.48);

  --accent: #b9f6c4;
  --accent-strong: #8eea9c;
  --accent-dark: #17351f;

  --success: #8eea9c;
  --warning: #f2cf70;
  --danger: #ff8f8f;
}
```

These are starting values, not mandatory exact values.

Avoid excessive bright green.

Green should be an accent rather than the entire interface.

---

## 3. Background

The application should have a dark cinematic background.

Preferred approach:

- Very dark green/black base
- Large blurred green radial gradients
- Subtle plant/nature image or texture where appropriate
- Soft vignette
- Low visual noise

Example concept:

```text
Dark background
       +
Soft green glow
       +
Plant imagery
       +
Dark translucent overlays
```

Do not use a completely flat black background.

Do not make the background so bright that white text loses contrast.

---

## 4. Main Application Container

Use a large centered container with rounded corners.

Characteristics:

- Maximum width around 1200–1400px
- Rounded corners around 24–32px
- Subtle border
- Dark translucent background
- Soft shadow
- Comfortable internal padding

Concept:

```text
┌──────────────────────────────────────────────┐
│                                              │
│   Navigation                                 │
│                                              │
│   Hero / Upload / Results                    │
│                                              │
│                                              │
└──────────────────────────────────────────────┘
```

On mobile, the container should use almost the full viewport width with smaller margins.

---

## 5. Navigation

Keep navigation minimal.

Suggested structure:

```text
[LOGO]        Features   How It Works   Plant Care       [Get Started ↗]
```

For this project, the branding should relate to the application.

Do not copy "LEANALYS" from the reference.

Possible project branding:

**PlantLens AI**

or

**LeafGuard AI**

or another appropriate original name.

The project title can remain:

**Plant Disease Prediction**

if preferred.

Navigation should:

- Be horizontally aligned
- Use small/medium typography
- Have generous spacing
- Use subtle hover transitions
- Avoid excessive navigation links

On mobile, collapse navigation appropriately.

---

## 6. Typography

Use a modern sans-serif font.

Preferred choices:

- Inter
- Manrope
- Outfit

Use one primary font family consistently.

Typography hierarchy:

### Hero heading

Very large:

```text
clamp(3rem, 7vw, 6.5rem)
```

Use:

- White/off-white
- Tight line height
- Slightly negative letter spacing
- Medium/semibold weight

Example style:

```text
See the health
of your plants.
```

The heading should occupy approximately 2–3 lines rather than becoming a giant paragraph.

### Supporting text

Use:

- 15–18px
- Muted white
- Comfortable line height
- Maximum width around 500px

### Cards

Use:

- 14–18px primary text
- 12–14px secondary text

Avoid excessive font-weight variation.

---

## 7. Hero Section

The hero should be the visual centerpiece.

Recommended structure:

```text
Small AI badge

Large headline

Supporting description

[Scan Your Plant ↗]

                       Visual plant image
                       +
                       AI analysis card
```

The hero should communicate immediately:

> Upload a plant image and let AI analyze its health.

Do not overload the hero with technical details.

---

## 8. AI Badge

Create a small pill above the hero heading.

Example:

```text
◉ AI POWERED PLANT HEALTH
```

Visual characteristics:

- Small
- Rounded pill
- Thin translucent border
- Dark transparent surface
- Light green accent
- Optional small leaf/AI icon

Do not use excessive glowing effects.

---

## 9. Primary CTA

The primary CTA should be visually prominent.

Example:

```text
[ ⊞  Scan Your Plant  ↗ ]
```

Style:

- Light green background
- Dark text
- Rounded pill
- Medium/semibold text
- Comfortable horizontal padding
- Subtle hover movement

Hover:

- Slight upward movement
- Slight brightness change
- Small arrow translation

Do not use aggressive animations.

---

## 10. Image Upload Experience

The upload component is one of the most important parts of the application.

Before upload:

```text
┌─────────────────────────────────────┐
│                                     │
│             [ Leaf icon ]           │
│                                     │
│        Drop your leaf image         │
│                                     │
│       or click to browse            │
│                                     │
│      JPG • JPEG • PNG               │
│                                     │
└─────────────────────────────────────┘
```

Use:

- Large rounded container
- Glass effect
- Dashed/subtle border
- Soft green hover state
- Clear drag-and-drop interaction

After upload:

Show:

- Image preview
- Filename
- File size
- Remove button
- Predict button

The uploaded image should be visually prominent.

---

## 11. Image Treatment

Plant images should look natural and high quality.

Use:

```css
object-fit: cover;
```

where appropriate.

Images should have:

- Rounded corners
- Subtle border
- Slight shadow
- Good aspect ratio

Do not distort uploaded images.

For result views, prefer:

```text
Original Image
+
Grad-CAM Explanation
```

side by side on desktop.

Stack them vertically on mobile.

---

## 12. Glassmorphism

Use glassmorphism carefully.

Recommended properties:

```css
background: rgba(20, 30, 23, 0.65);
backdrop-filter: blur(18px);
border: 1px solid rgba(255, 255, 255, 0.1);
```

Use glass effects for:

- Navigation
- Upload card
- Result cards
- AI information cards
- Floating status cards

Do not apply glassmorphism to every element.

---

## 13. Result Card

After prediction, show a strong result card.

Example:

```text
┌─────────────────────────────────────────────┐
│  ✦ DETECTED DISEASE                         │
│                                             │
│  Grape — Black Rot                          │
│                                             │
│  Confidence                                 │
│  ████████████████████░░  99.99%             │
│                                             │
│  AI-generated prediction                    │
└─────────────────────────────────────────────┘
```

The disease name should be the strongest piece of information.

Convert dataset labels such as:

```text
Grape___Black_rot
```

into user-friendly display text:

```text
Grape — Black Rot
```

Do not alter the actual class label used by the model.

---

## 14. Confidence Visualization

Display confidence as:

- Percentage
- Progress bar or circular indicator

Example:

```text
Confidence

████████████████████░  99.9%
```

Use the accent color.

Do not imply that confidence equals real-world diagnostic certainty.

Recommended supporting text:

> Model confidence

rather than:

> Diagnosis certainty

---

## 15. Grad-CAM Section

Grad-CAM should have its own visually important section.

Suggested heading:

```text
Why the AI made this prediction
```

Supporting text:

> Grad-CAM highlights image regions that contributed strongly to the model's prediction.

Display:

```text
┌───────────────────┐   ┌───────────────────┐
│ Original Image    │   │ AI Explanation    │
│                   │   │                   │
│       IMAGE       │   │     HEATMAP       │
│                   │   │                   │
└───────────────────┘   └───────────────────┘
```

Optional toggle:

```text
[ Original ] [ Grad-CAM ] [ Compare ]
```

The Grad-CAM explanation must remain technically accurate.

Do not label it:

> Exact disease location

Instead use:

> Model attention / contributing regions

---

## 16. Floating AI Information Cards

The reference image uses floating cards over imagery.

This design can be adapted for this project.

Example:

```text
┌───────────────────────────┐
│ ✦ AI ANALYSIS             │
│                           │
│ Grape Black Rot           │
│                           │
│ Confidence       99.9%    │
│ ████████████████████      │
└───────────────────────────┘
```

Use these sparingly.

Cards should not obstruct important image content.

---

## 17. How It Works Section

Create a clean three-step section.

```text
01              02                 03

UPLOAD          ANALYZE            EXPLAIN

Upload a        EfficientNetB0     View the
leaf image.     analyzes it.       Grad-CAM.
```

Use simple icons.

Keep explanations short.

This section should help a recruiter/user understand the pipeline quickly.

---

## 18. Technical Section

Do not place technical details in the hero.

Create a separate section for:

```text
Powered by Deep Learning

EfficientNetB0
38 Plant Diseases
Grad-CAM
FastAPI
React
```

This gives the project technical credibility without making the first screen feel like documentation.

---

## 19. Animations

Animations should be subtle.

Recommended:

- Fade-in
- Slight slide-up
- Button hover
- Card hover
- Image reveal
- Progress bar animation
- Grad-CAM result reveal

Timing:

```text
150–400ms
```

Use easing such as:

```css
ease-out
```

Avoid:

- Excessive bouncing
- Continuous animations everywhere
- Flashing
- Heavy parallax
- Long loading animations

The interface should feel fast.

---

## 20. Loading State

During prediction, show a premium but simple loading state.

Possible:

```text
Analyzing your plant...

[ animated scanning line ]

EfficientNetB0 is processing the image
```

Do not fake a long processing time.

The animation should reflect actual request state.

---

## 21. Error State

Errors should fit the visual system.

Example:

```text
Something went wrong

We couldn't analyze this image.

[ Try Again ]
```

Use subtle red/pink accents.

Do not display:

```text
Traceback...
ConnectionRefusedError...
500 Internal Server Error...
```

to normal users.

---

## 22. Responsive Design

Desktop:

```text
Large hero
Two-column layouts
Floating cards
Large imagery
```

Tablet:

```text
Reduced typography
Two-column sections where possible
```

Mobile:

```text
Single-column layout
Collapsed navigation
Full-width upload area
Stacked image comparison
Readable heading
Large touch targets
```

Never allow horizontal scrolling.

Test at:

- 1440px
- 1024px
- 768px
- 390px

---

## 23. Accessibility

Maintain:

- Strong text contrast
- Visible keyboard focus
- Proper button labels
- Alt text for images
- Semantic HTML
- Accessible upload control
- Clear error messages

Do not sacrifice accessibility for visual effects.

---

## 24. Spacing

Use a consistent spacing system.

Suggested values:

```text
4px
8px
12px
16px
24px
32px
48px
64px
96px
128px
```

Hero sections should have generous vertical spacing.

Avoid cramped layouts.

---

## 25. Border Radius

Use rounded UI consistently.

Suggested:

```text
Buttons: 999px
Small pills: 999px
Cards: 20–28px
Large containers: 28–32px
Image cards: 18–24px
```

Avoid mixing many unrelated radius values.

---

## 26. Shadows

Use soft shadows rather than harsh black shadows.

Example concept:

```css
box-shadow:
  0 20px 60px rgba(0, 0, 0, 0.35);
```

Do not overuse shadows.

Glass cards can use subtle shadows combined with borders.

---

## 27. Icons

Use one consistent icon style.

Possible library:

- Lucide React

Use icons for:

- Upload
- Leaf
- Arrow
- Sparkles
- Image
- Refresh
- Info
- Check
- Alert

Do not use random emoji icons throughout the UI.

Small decorative symbols are acceptable if they fit the design.

---

## 28. Avoid These Design Problems

Do NOT create:

- Generic Bootstrap-looking dashboard
- White corporate admin panel
- Excessive cards
- Excessive gradients
- Neon green cyberpunk design
- Huge technical text blocks
- Random colorful icons
- Excessive shadows
- Excessive glassmorphism
- Poor contrast
- Tiny upload controls
- Overly complicated navigation
- Cluttered hero section

The result should feel **premium and calm**, not flashy.

---

## 29. Reference Image Interpretation

The reference image communicates these principles:

```text
Dark cinematic environment
        +
Nature photography
        +
Large typography
        +
Glass UI
        +
Green accent
        +
Minimal navigation
        +
Floating AI information
        +
Strong CTA
```

Use these principles as inspiration.

Do not copy:

- Brand name
- Logo
- Exact text
- Exact imagery
- Exact card placement
- Exact typography
- Exact website identity

Create an original interface for the Plant Disease Prediction project.

---

## 30. Priority Order

When making visual decisions, prioritize:

1. Usability
2. Readability
3. Clear AI workflow
4. Responsive behavior
5. Visual hierarchy
6. Accessibility
7. Premium aesthetics
8. Animation

A beautiful interface that is difficult to use is not acceptable.

---

## 31. Final Visual Goal

The finished frontend should feel like:

> A premium AI plant-health product where a user can immediately understand what the system does, upload a leaf image, receive a prediction, and visually understand why the model made that prediction.

The first impression should be:

**Modern + Natural + AI + Trustworthy + Premium.**
