from pywinauto.application import Application

def test_01():
    app = Application(backend="uia").start("notepad.exe")
    app.UntitledNotepad.type_keys("%FX")

def test_02():
    """windowSpecification 窗口规范"""
    app = Application(backend="uia").start(r'D:\Program_all\tool\Sublime Text\sublime_text.exe')
    dlg_spec = app.window(title='untitled • - Sublime Text')
    print(dlg_spec)

    wo = dlg_spec.wrapper_object()
    print(wo)

    # 可以是多层次的
    dl = app.window(title_re='.* - Notepad$').window(class_name='Edit')
    print(dl)

def test_03():
    """属性解析魔法"""
    app = Application(backend="uia").start(r'D:\Program_all\tool\Sublime Text\sublime_text.exe')
    dlg_spec = app.window(best_match='untitled • - Sublime Text')
    print(dlg_spec)

    # is equivalent to 
    dl_01= app['untitled • - Sublime Text'] 
    print(dl_01)
    dl_02 = app.untitledSublimeText  
    print(dl_02)
    dl_03 = app.window(best_match='untitledSublimeText')
    print(dl_03)

def test_04():
    app = Application(backend="uia").start(r'D:\Program_all\tool\Sublime Text\sublime_text.exe')
    dlg_spec = app.window(best_match='untitled • - Sublime Text')
    app.untitledSublimeText.print_control_identifiers(filename='pci.txt')

def test_05():
    """禁用魔法属性"""
    # app = Application(backend="uia").start(r'D:\Program_all\tool\Sublime Text\sublime_text.exe')
    # dl = app.untitledSublimeText  
    # print(dl)
    print("禁用魔法属性")
    app = Application(backend="uia",allow_magic_lookup=False).start(r'D:\Program_all\tool\Sublime Text\sublime_text.exe')
    d2 = app.untitledSublimeText  
    print(d2)

def test_06():
    a = Application()
    app = a.start('Notepad.exe')
    print(app)
    app.UntitledNotepad.draw_outline()
    app.UntitledNotepad.menu_select("Edit -> Replace")
    app.Replace.print_control_identifiers()

if __name__ == "__main__":
    test_06()    