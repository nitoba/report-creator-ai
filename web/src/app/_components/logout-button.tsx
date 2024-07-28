'use client'

import { logoutAction } from '../_actions/logout-action'
import { DropdownMenuItem } from './ui/dropdown-menu'

export function LogoutButton() {
  function handleLogout() {
    logoutAction()
  }
  return <DropdownMenuItem onClick={handleLogout}>Logout</DropdownMenuItem>
}
