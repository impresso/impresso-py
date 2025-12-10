import base64
import struct
from typing import List


def embedding_to_vector(embedding: str) -> List[float]:
    """
    Convert a base64-encoded embedding string to an array of floats.

    The embedding string is expected to be in the format: <model>:<base64-encoded vector>
    where the base64-encoded part represents an array of float32 values.

    Args:
        embedding: A string in the format "<model>:<base64-encoded vector>"
                  (e.g., "clip-ViT-B-32:AAAAAAAAAAAAAAAA...")

    Returns:
        A list of float values representing the embedding vector

    Raises:
        ValueError: If the embedding string format is invalid

    Example:
        >>> embedding = "clip-ViT-B-32:AAAAAAAAAAAAAAAA..."
        >>> vector = embedding_to_vector(embedding)
        >>> print(vector)
        [0.0, 0.0, 0.0, ...]
    """
    if ':' not in embedding:
        raise ValueError(
            "Invalid embedding format. Expected '<model>:<base64-encoded vector>'"
        )

    # Split the model prefix from the base64-encoded vector
    _, base64_vector = embedding.split(':', 1)

    # Decode the base64 string to bytes
    vector_bytes = base64.b64decode(base64_vector)

    # Convert bytes to array of float32 values
    # Each float32 is 4 bytes, so we calculate the number of floats
    num_floats = len(vector_bytes) // 4

    # Unpack the bytes as little-endian float32 values
    vector = list(struct.unpack(f'<{num_floats}f', vector_bytes))

    return vector


def vector_to_embedding(vector: List[float], model: str) -> str:
    """
    Convert an array of floats to a base64-encoded embedding string with model prefix.

    Args:
        vector: A list of float values representing the embedding vector
        model: The model identifier to use as prefix (e.g., "clip-ViT-B-32")

    Returns:
        A string in the format "<model>:<base64-encoded vector>"

    Example:
        >>> vector = [0.0, 0.1, 0.2, 0.3]
        >>> embedding = vector_to_embedding(vector, "clip-ViT-B-32")
        >>> print(embedding)
        clip-ViT-B-32:AAAAAAAAAAAAAAAA...
    """
    # Pack the float values as little-endian float32 bytes
    vector_bytes = struct.pack(f'<{len(vector)}f', *vector)

    # Encode the bytes as base64
    base64_vector = base64.b64encode(vector_bytes).decode('ascii')

    # Combine model prefix with base64-encoded vector
    embedding = f"{model}:{base64_vector}"

    return embedding
