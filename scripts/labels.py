"""Human-readable labels for the coded values in the review dataset.

Any value not listed here falls back to underscore-to-space title case.
"""

LABELS = {
    "workflow_stage": {
        "diagnosis": "Diagnosis",
        "education": "Education",
        "training": "Training",
        "planning": "Planning",
        "intraoperative": "Intraoperative",
        "method_development": "Method Development",
        "multi_task": "Multi-task",
        "not_specified": "Not Specified",
    },
    "specialty": {
        "abdominal": "Abdominal",
        "breast": "Breast",
        "cardiothoracic": "Cardiothoracic",
        "education": "Education",
        "general": "General",
        "gynecology": "Gynecology",
        "head_and_neck": "Head & Neck",
        "mixed": "Mixed",
        "neurosurgery": "Neurosurgery",
        "not_specified": "Not Specified",
        "oncologic": "Oncologic",
        "ophthalmic": "Ophthalmic",
        "oral_maxillofacial": "Oral & Maxillofacial",
        "orthopedic": "Orthopedic",
        "other": "Other",
        "pediatric_surgery": "Pediatric Surgery",
        "plastic": "Plastic",
        "urology": "Urology",
        "vascular": "Vascular",
    },
    "evaluation_target": {
        "animal": "Animal",
        "cadaver": "Cadaver",
        "dataset": "Dataset",
        "human_subject": "Human Subject",
        "mixed": "Mixed",
        "not_specified": "Not Specified",
        "patient": "Patient",
        "phantom": "Phantom",
        "virtual": "Virtual",
    },
    "device": {
        "aerial_imaging_plate": "Aerial Imaging Plate",
        "autostereoscopic_3d_display": "Autostereoscopic 3D Display",
        "body_handheld": "Handheld Device",
        "hmd_ost": "HMD (Optical See-Through)",
        "hmd_vst": "HMD (Video See-Through)",
        "microscope": "Microscope",
        "multiple_devices": "Multiple Devices",
        "spatial_monitor": "Spatial Monitor",
        "spatial_projection": "Spatial Projection",
        "spatial_projection_semtransparent": "Semi-transparent Projection",
    },
    "dimensionality": {
        "2d": "2D",
        "2d_3d": "2D + 3D",
        "3d": "3D",
        "4d": "4D",
        "mixed": "Mixed",
        "multimodal": "Multimodal",
        "not_specified": "Not Specified",
    },
    "image_modalities": {
        "angiography": "Angiography",
        "cbct": "CBCT",
        "ct": "CT",
        "dti": "DTI",
        "hsi": "HSI",
        "mri": "MRI",
        "multimodal": "Multimodal",
        "not_specified": "Not Specified",
        "oct": "OCT",
        "pet": "PET",
        "photoacoustic": "Photoacoustic",
        "rgb": "RGB Camera",
        "spect": "SPECT",
        "thermal": "Thermal",
        "us": "Ultrasound",
        "xray": "X-ray",
    },
    "rendering_type": {
        "no_post_processing": "No Post-processing",
        "not_reported": "Not Reported",
        "other_process": "Other Process",
        "surface_modeling": "Surface Modeling",
        "volume_rendering": "Volume Rendering",
    },
    "anchoring_context": {
        "in_situ": "In-situ",
        "inter_situ": "Inter-situ",
        "off_situ": "Off-situ",
    },
    "registration_method": {
        "manual": "Manual",
        "marker_optical": "Optical Marker",
        "marker_other": "Other Marker",
        "markerless": "Markerless",
    },
}

# Columns whose values may contain several pipe-separated labels.
MULTI_LABEL_COLUMNS = [
    "workflow_stage",
    "evaluation_target",
    "image_modalities",
    "anchoring_context",
    "perception_cues",
    "aux_visualization_content",
]


def label(column, value):
    """Return the display label for one coded value."""
    if value is None or (isinstance(value, float)):
        return value
    value = str(value).strip()
    mapped = LABELS.get(column, {}).get(value)
    if mapped is not None:
        return mapped
    return value.replace("_", " ").title()


def label_series(series, column):
    """Vectorised version of label() for a pandas Series."""
    return series.map(lambda v: label(column, v))
