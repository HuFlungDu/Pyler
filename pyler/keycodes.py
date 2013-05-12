import win32con
import string

mod_shift,mod_control,mod_alt,mod_super = win32con.MOD_SHIFT, win32con.MOD_CONTROL, win32con.MOD_ALT, win32con.MOD_WIN
k_Up, k_Down, k_Left, k_Right = win32con.VK_UP,win32con.VK_DOWN,win32con.VK_LEFT,win32con.VK_RIGHT
k_a,k_b,k_c,k_d,k_e,k_f,k_g,k_h,k_i,k_j,k_k,k_l,k_m,k_n,k_o,k_p,k_q,k_r,k_s,k_t,k_u,k_v,k_w,k_x,k_y,k_z = (ord(x) for x in string.ascii_uppercase)
k_Comma, k_Period = 0xBC, 0xBE
k_1,k_2,k_3,k_4,k_5,k_6,k_7,k_8,k_9 = (ord(x) for x in "123456789")
k_Home, k_End, k_PgUp, k_PgDn, k_Insert, k_Space, k_Return, k_Enter,k_BackSpace,k_Tab,k_Clear,k_Pause,k_Escape,k_Delete = win32con.VK_HOME, win32con.VK_END, win32con.VK_PRIOR, win32con.VK_NEXT, win32con.VK_INSERT, win32con.VK_SPACE, win32con.VK_RETURN, win32con.VK_RETURN, win32con.VK_BACK,win32con.VK_TAB,win32con.VK_CLEAR,win32con.VK_PAUSE,win32con.VK_ESCAPE,win32con.VK_DELETE
k_KP_0,k_KP_1,k_KP_2,k_KP_3,k_KP_4,k_KP_5,k_KP_6,k_KP_7,k_KP_8,k_KP_9 = win32con.VK_NUMPAD0, win32con.VK_NUMPAD1, win32con.VK_NUMPAD2, win32con.VK_NUMPAD3, win32con.VK_NUMPAD4, win32con.VK_NUMPAD5, win32con.VK_NUMPAD6, win32con.VK_NUMPAD7, win32con.VK_NUMPAD8, win32con.VK_NUMPAD9
k_F1,k_F2,k_F3,k_F4,k_F5,k_F6,k_F7,k_F8,k_F9,k_F10,k_F11,k_F12,k_F13,k_F14,k_F15,k_F16,k_F17,k_F18,k_F19,k_F20,k_F21,k_F22,k_F23,k_24 = win32con.VK_F1,win32con.VK_F2,win32con.VK_F3,win32con.VK_F4,win32con.VK_F5,win32con.VK_F6,win32con.VK_F7,win32con.VK_F8,win32con.VK_F9,win32con.VK_F10,win32con.VK_F11,win32con.VK_F12,win32con.VK_F13,win32con.VK_F14,win32con.VK_F15,win32con.VK_F16,win32con.VK_F17,win32con.VK_F18,win32con.VK_F19,win32con.VK_F20,win32con.VK_F21,win32con.VK_F22,win32con.VK_F23,win32con.VK_F24
