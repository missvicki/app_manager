import React from "react";

import * as FaIcons from "react-icons/fa";
import * as AiIcons from "react-icons/ai";
import * as IoIcons from "react-icons/io";

export const SidebarData = [
    {
    title: "Login",
    path: "/login",        
    icon: <FaIcons.FaUserCircle />,
    cName: "nav-text"
    },
    {
    title: "Home",
    path: "/",
    icon: <AiIcons.AiFillHome />,
    cName: "nav-text"
  },
  {
    title: "Settings",
    path: "/settings",
    icon: <IoIcons.IoMdSettings />,
    cName: "nav-text"
  },
  {
    title: "Information",
    path: "/info",
    icon: <AiIcons.AiFillInfoCircle />,
    cName: "nav-text"
  }
];
