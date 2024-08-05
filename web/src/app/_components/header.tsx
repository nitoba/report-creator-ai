import { Sheet, SheetContent, SheetTrigger } from './ui/sheet'
import { Menu, Search } from 'lucide-react'
import { Button } from './ui/button'
import { Input } from './ui/input'
import { UserMenu } from './user-menu'

import { Breadcrumbs } from './breadcrumbs'
import { Sidebar } from './sidebar'

export function Header() {
  return (
    <header className="flex h-14 items-center gap-4 border-b bg-muted/40 px-4 lg:h-[60px] lg:px-6">
      <Sheet>
        <SheetTrigger asChild>
          <Button variant="outline" size="icon" className="shrink-0 md:hidden">
            <Menu className="h-5 w-5" />
            <span className="sr-only">Toggle navigation menu</span>
          </Button>
        </SheetTrigger>
        <SheetContent side="left" className="flex flex-col">
          <Sidebar isInSheet />
        </SheetContent>
      </Sheet>
      <div className="w-full flex-1 flex items-center gap-4">
        <Breadcrumbs />
        <form className="ml-auto">
          <div className="relative w-full">
            <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
            <Input
              type="search"
              placeholder="Search reports..."
              className="w-full flex-1 appearance-none bg-background pl-8 shadow-none md:w-2/3 lg:w-[400px]"
            />
          </div>
        </form>
      </div>
      <UserMenu />
    </header>
  )
}
