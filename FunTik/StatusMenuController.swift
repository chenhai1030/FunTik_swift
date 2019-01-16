//
//  StatusMenuController.swift
//  FunTik
//
//  Created by chenhai on 2019/1/4.
//  Copyright © 2019 chenhai. All rights reserved.
//

import Cocoa

class StatusMenuController: NSObject {
    @IBOutlet weak var statusMenu: NSMenu!
    
    let statusItem = NSStatusBar.system.statusItem(withLength: NSStatusItem.variableLength)
    
    override func awakeFromNib() {
        let icon = NSImage(named: "statusIcon")
        statusItem.image = icon
        statusItem.menu = statusMenu
    }
    
    @IBAction func quitClicked(sender: NSMenuItem) {
        NSApplication.shared.terminate(self)
    }
}
