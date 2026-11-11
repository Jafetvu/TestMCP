using UnityEditor;
using UnityEngine;

namespace Firefly.EditorTools
{
    [InitializeOnLoad]
    public static class GameSetupTools
    {
        static GameSetupTools()
        {
            Debug.Log("[Firefly] GameSetupTools initialized successfully in Unity Editor!");
        }

        [MenuItem("Luciérnaga/Ping")]
        public static void Ping()
        {
            Debug.Log("[Firefly] Pong from Luciérnaga!");
        }
    }
}
