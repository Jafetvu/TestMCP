using UnityEngine;

namespace Firefly.Environment
{
    /// <summary>
    /// Moving platform that oscillates between two positions,
    /// carrying the player safely over chasms and hazards.
    /// Follows the Single Responsibility Principle: handles kinematic platform movement and passenger attachment.
    /// </summary>
    [RequireComponent(typeof(Collider2D))]
    public class MovingPlatform : MonoBehaviour
    {
        [Header("Movement Path")]
        [Tooltip("Relative target offset from start position.")]
        [SerializeField] private Vector2 moveOffset = new Vector2(4f, 0f);

        [Tooltip("Speed of movement.")]
        [SerializeField] private float speed = 2.0f;

        [Tooltip("Pause duration at each end in seconds.")]
        [SerializeField] private float waitTimeAtEnds = 0.5f;

        private Vector3 startPos;
        private Vector3 targetPos;
        private bool movingToTarget = true;
        private float waitTimer;

        private void Start()
        {
            startPos = transform.position;
            targetPos = startPos + (Vector3)moveOffset;
        }

        private void Update()
        {
            if (waitTimer > 0f)
            {
                waitTimer -= Time.deltaTime;
                return;
            }

            Vector3 destination = movingToTarget ? targetPos : startPos;
            transform.position = Vector3.MoveTowards(transform.position, destination, speed * Time.deltaTime);

            if (Vector3.Distance(transform.position, destination) < 0.01f)
            {
                movingToTarget = !movingToTarget;
                waitTimer = waitTimeAtEnds;
            }
        }

        private void OnCollisionEnter2D(Collision2D collision)
        {
            // Parent the player so they ride the platform
            if (collision.gameObject.CompareTag("Player") && collision.transform.position.y > transform.position.y)
            {
                collision.transform.SetParent(transform);
            }
        }

        private void OnCollisionExit2D(Collision2D collision)
        {
            // Unparent when jumping off
            if (collision.gameObject.CompareTag("Player"))
            {
                collision.transform.SetParent(null);
            }
        }

        private void OnDrawGizmosSelected()
        {
            Gizmos.color = Color.cyan;
            Vector3 origin = Application.isPlaying ? startPos : transform.position;
            Gizmos.DrawLine(origin, origin + (Vector3)moveOffset);
            Gizmos.DrawWireCube(origin + (Vector3)moveOffset, transform.localScale);
        }
    }
}
