using UnityEngine;
#if ENABLE_INPUT_SYSTEM
using UnityEngine.InputSystem;
#endif

namespace Firefly.Core
{
    /// <summary>
    /// Centralized input helper supporting the Unity New Input System
    /// with graceful fallbacks for Keyboard, Gamepad and legacy input.
    /// </summary>
    public static class GameInput
    {
        public static float GetHorizontal()
        {
#if ENABLE_INPUT_SYSTEM
            float move = 0f;
            if (Keyboard.current != null)
            {
                if (Keyboard.current.aKey.isPressed || Keyboard.current.leftArrowKey.isPressed)
                    move -= 1f;
                if (Keyboard.current.dKey.isPressed || Keyboard.current.rightArrowKey.isPressed)
                    move += 1f;
            }

            if (Gamepad.current != null)
            {
                float stick = Gamepad.current.leftStick.x.ReadValue();
                if (Mathf.Abs(stick) > 0.15f)
                    move = stick;
                else if (Gamepad.current.dpad.left.isPressed)
                    move -= 1f;
                else if (Gamepad.current.dpad.right.isPressed)
                    move += 1f;
            }

            return Mathf.Clamp(move, -1f, 1f);
#else
            return Input.GetAxisRaw("Horizontal");
#endif
        }

        public static float GetVertical()
        {
#if ENABLE_INPUT_SYSTEM
            float move = 0f;
            if (Keyboard.current != null)
            {
                if (Keyboard.current.sKey.isPressed || Keyboard.current.downArrowKey.isPressed)
                    move -= 1f;
                if (Keyboard.current.wKey.isPressed || Keyboard.current.upArrowKey.isPressed)
                    move += 1f;
            }

            if (Gamepad.current != null)
            {
                float stick = Gamepad.current.leftStick.y.ReadValue();
                if (Mathf.Abs(stick) > 0.15f)
                    move = stick;
                else if (Gamepad.current.dpad.down.isPressed)
                    move -= 1f;
                else if (Gamepad.current.dpad.up.isPressed)
                    move += 1f;
            }

            return Mathf.Clamp(move, -1f, 1f);
#else
            return Input.GetAxisRaw("Vertical");
#endif
        }

        public static bool GetJumpDown()
        {
#if ENABLE_INPUT_SYSTEM
            bool jump = false;
            if (Keyboard.current != null)
            {
                jump = Keyboard.current.spaceKey.wasPressedThisFrame ||
                       Keyboard.current.wKey.wasPressedThisFrame ||
                       Keyboard.current.upArrowKey.wasPressedThisFrame;
            }

            if (!jump && Gamepad.current != null)
            {
                jump = Gamepad.current.buttonSouth.wasPressedThisFrame;
            }

            return jump;
#else
            return Input.GetButtonDown("Jump") || Input.GetKeyDown(KeyCode.Space) || Input.GetKeyDown(KeyCode.W);
#endif
        }

        public static bool GetJumpHeld()
        {
#if ENABLE_INPUT_SYSTEM
            bool jump = false;
            if (Keyboard.current != null)
            {
                jump = Keyboard.current.spaceKey.isPressed ||
                       Keyboard.current.wKey.isPressed ||
                       Keyboard.current.upArrowKey.isPressed;
            }

            if (!jump && Gamepad.current != null)
            {
                jump = Gamepad.current.buttonSouth.isPressed;
            }

            return jump;
#else
            return Input.GetButton("Jump") || Input.GetKey(KeyCode.Space) || Input.GetKey(KeyCode.W);
#endif
        }

        public static bool GetPauseDown()
        {
#if ENABLE_INPUT_SYSTEM
            bool pause = false;
            if (Keyboard.current != null)
            {
                pause = Keyboard.current.escapeKey.wasPressedThisFrame ||
                        Keyboard.current.pKey.wasPressedThisFrame;
            }

            if (!pause && Gamepad.current != null)
            {
                pause = Gamepad.current.startButton.wasPressedThisFrame;
            }

            return pause;
#else
            return Input.GetKeyDown(KeyCode.Escape) || Input.GetKeyDown(KeyCode.P);
#endif
        }

        public static bool GetRetryDown()
        {
#if ENABLE_INPUT_SYSTEM
            bool retry = false;
            if (Keyboard.current != null)
            {
                retry = Keyboard.current.rKey.wasPressedThisFrame ||
                        Keyboard.current.enterKey.wasPressedThisFrame ||
                        Keyboard.current.numpadEnterKey.wasPressedThisFrame;
            }

            if (!retry && Gamepad.current != null)
            {
                retry = Gamepad.current.buttonSouth.wasPressedThisFrame;
            }

            return retry;
#else
            return Input.GetKeyDown(KeyCode.R) || Input.GetKeyDown(KeyCode.Return);
#endif
        }
    }
}
