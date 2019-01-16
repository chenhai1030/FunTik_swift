//
//  WindowController.swift
//  FunTik
//
//  Created by chenhai on 2019/1/11.
//  Copyright © 2019 chenhai. All rights reserved.
//

import Foundation
import Cocoa

class WindowController: NSWindowController {
    override func windowWillLoad(){
        (NSApplication.sharedApplication().delegate as! AppDelegate).window = self.window
    }

}
