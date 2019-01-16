//
//  main.swift
//  FunTik
//
//  Created by chenhai on 2019/1/15.
//  Copyright © 2019 chenhai. All rights reserved.
//

// Application main entry point

import Foundation
import Cocoa


let path = Bundle.main.path(forResource: "Bridge", ofType: "plugin")
guard let pluginbundle = Bundle(path: path!) else {
    fatalError("Could not load python plugin bundle")
}
pluginbundle.load()

// Load the principal class
guard let pc = pluginbundle.principalClass as? BridgeInterface.Type else {
    fatalError("Could not load principal class from python bundle")
}

//// Create an instance of the principal class and store it
let interface = pc.createInstance()
Bridge.setSharedInstance(to: interface)
//let pythonMessage = Bridge.sharedInstance().getPythonInformation()
//Swift.print("Info from python:\n\(pythonMessage)")

let ret = NSApplicationMain(CommandLine.argc, CommandLine.unsafeArgv)
exit(ret)
