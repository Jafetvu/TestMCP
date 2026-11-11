using UnityEngine;

namespace Firefly.Core
{
    /// <summary>
    /// Smooth 2D camera follow for the firefly player with configurable offset and deadzone.
    /// Follows the Single Responsibility Principle: handles camera positioning relative to the target.
    /// </summary>
    public class CameraFollow2D : MonoBehaviour
    {
        [Header("Target & Tracking")]
        [Tooltip("Target transform to follow. If null, automatically locates the GameObject tagged 'Player'.")]
        [SerializeField] private Transform target;

        [Tooltip("Offset relative to the player position.")]
        [SerializeField] private Vector3 offset = new Vector3(0f, 1f, -10f);

        [Tooltip("Smooth damp time for camera lag / fluidity.")]
        [SerializeField] private float smoothTime = 0.2f;

        [Header("Level Bounds (Optional)")]
        [SerializeField] private bool useBounds = false;
        [SerializeField] private Vector2 minBounds = new Vector2(-10f, -5f);
        [SerializeField] private Vector2 maxBounds = new Vector2(50f, 20f);

        private Vector3 currentVelocity;

        private void Start()
        {
            if (target == null)
            {
                FindPlayer();
            }

            if (target != null)
            {
                transform.position = target.position + offset;
            }
        }

        private void LateUpdate()
        {
            if (target == null)
            {
                FindPlayer();
                if (target == null) return;
            }

            Vector3 targetPosition = target.position + offset;

            if (useBounds)
            {
                targetPosition.x = Mathf.Clamp(targetPosition.x, minBounds.x, maxBounds.x);
                targetPosition.y = Mathf.Clamp(targetPosition.y, minBounds.y, maxBounds.y);
            }

            transform.position = Vector3.SmoothDamp(transform.position, targetPosition, ref currentVelocity, smoothTime);
        }

        private void FindPlayer()
        {
            GameObject player = GameObject.FindWithTag("Player");
            if (player != null)
            {
                target = player.transform;
            }
        }
    }
}
