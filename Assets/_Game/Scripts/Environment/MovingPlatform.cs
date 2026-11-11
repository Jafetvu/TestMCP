using UnityEngine;

namespace Firefly.Environment
{
    /// <summary>
    /// Kinematic platform that oscillates between its start position and an offset.
    /// Exposes its current velocity so the player can ride it (see PlayerController).
    /// Follows the Single Responsibility Principle: handles platform movement only.
    /// </summary>
    [RequireComponent(typeof(Collider2D))]
    public class MovingPlatform : MonoBehaviour
    {
        [Header("Movement Path")]
        [Tooltip("Target offset relative to the start position.")]
        [SerializeField] private Vector2 moveOffset = new Vector2(4f, 0f);

        [Tooltip("Movement speed in units per second.")]
        [SerializeField] private float speed = 2.0f;

        [Tooltip("Pause duration at each end, in seconds.")]
        [SerializeField] private float waitTimeAtEnds = 0.5f;

        private Rigidbody2D rb;
        private Vector2 startPos;
        private Vector2 targetPos;
        private bool movingToTarget = true;
        private float waitTimer;

        /// <summary>Current platform velocity in world units per second.</summary>
        public Vector2 Velocity { get; private set; }

        private void Awake()
        {
            // A kinematic body gives correct collision response when the platform moves.
            rb = GetComponent<Rigidbody2D>();
            if (rb == null)
                rb = gameObject.AddComponent<Rigidbody2D>();

            rb.bodyType = RigidbodyType2D.Kinematic;
            rb.interpolation = RigidbodyInterpolation2D.Interpolate;
            rb.constraints = RigidbodyConstraints2D.FreezeRotation;

            startPos = rb.position;
            targetPos = startPos + moveOffset;
        }

        private void FixedUpdate()
        {
            if (waitTimer > 0f)
            {
                waitTimer -= Time.fixedDeltaTime;
                Velocity = Vector2.zero;
                return;
            }

            Vector2 destination = movingToTarget ? targetPos : startPos;
            Vector2 next = Vector2.MoveTowards(rb.position, destination, speed * Time.fixedDeltaTime);
            Velocity = (next - rb.position) / Time.fixedDeltaTime;
            rb.MovePosition(next);

            if ((next - destination).sqrMagnitude < 0.0001f)
            {
                movingToTarget = !movingToTarget;
                waitTimer = waitTimeAtEnds;
            }
        }

        private void OnDrawGizmosSelected()
        {
            Gizmos.color = Color.cyan;
            Vector3 origin = Application.isPlaying ? (Vector3)startPos : transform.position;
            Gizmos.DrawLine(origin, origin + (Vector3)moveOffset);
            Gizmos.DrawWireCube(origin + (Vector3)moveOffset, transform.localScale);
        }
    }
}
