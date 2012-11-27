import sublime, sublime_plugin

markPreffix = "delphi_style_bookmark_"

class SetDelphiBookmarkCommand(sublime_plugin.TextCommand):
   def run(self, edit, key, icon='bookmark'):

      markId = markPreffix + str(key)

      if len(self.view.sel()) > 0:

         mark = self.view.sel()[0]

         for i in range(9):
            regions = self.view.get_regions(markPreffix+str(i))

            if len(regions) == 0:
               continue

            m = regions[0]

            if mark.intersects(m):
               self.view.erase_regions(markPreffix+str(i))

               if i == key:
                  return

         mark = self.adapt_region(mark)

         self.view.add_regions(markId,
                               [mark],
                               markId,
                               icon,
                               sublime.HIDDEN | sublime.PERSISTENT)

   def adapt_region(self, init_region):
      row, _ = self.view.rowcol(init_region.begin())

      point = self.view.text_point(row, 0)

      return sublime.Region(point, point)

class GoToDelphiBookmarkCommand(sublime_plugin.TextCommand):
   def run(self, edit, key):

      markId = "delphi_style_bookmark_" + str(key)

      regions = self.view.get_regions(markId)

      if len(regions) > 0:
         # set bookmark to a center of the screen
         self.view.show_at_center(regions[0])

         # set cursor to the proper position
         self.view.sel().clear()
         self.view.sel().add(regions[0])