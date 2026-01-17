"""promptune-HtmlGraph Integration Layer.

This package provides shared models, configuration, and utilities
for tight integration between promptune and HtmlGraph.
"""

from .config import (
    promptuneConfig,
    DashboardConfig,
    HtmlGraphConfig,
    IntegrationConfig,
    IntentDetectionConfig,
    ParallelExecutionConfig,
    TrackingConfig,
    UnifiedConfig,
)
from .config_loader import (
    ConfigLoader,
    get_config,
    reload_config,
)
from .models import (
    promptuneSession,
    IntegrationHealth,
    IntentDetection,
    ParallelExecution,
    ParallelTask,
    TrackMetadata,
    WorkAttribution,
)
from .types import (
    DetectionMethod,
    ExecutionMode,
    IntegrationStatus,
    Priority,
    TaskStatus,
    TrackingEvent,
    WorkType,
)

__all__ = [
    # Config classes
    "UnifiedConfig",
    "promptuneConfig",
    "HtmlGraphConfig",
    "IntegrationConfig",
    "IntentDetectionConfig",
    "ParallelExecutionConfig",
    "TrackingConfig",
    "DashboardConfig",
    # Config loader
    "ConfigLoader",
    "get_config",
    "reload_config",
    # Model classes
    "promptuneSession",
    "IntentDetection",
    "ParallelExecution",
    "ParallelTask",
    "WorkAttribution",
    "TrackMetadata",
    "IntegrationHealth",
    # Type definitions
    "ExecutionMode",
    "DetectionMethod",
    "WorkType",
    "TaskStatus",
    "Priority",
    "TrackingEvent",
    "IntegrationStatus",
]

__version__ = "0.1.0"
