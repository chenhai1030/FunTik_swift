//
//  BridgeInterface.swift
//  FunTik
//
//  Created by chenhai on 2019/1/14.
//  Copyright © 2019 chenhai. All rights reserved.
//

import Foundation

/// A simple demonstration interface to the python module
@objc public protocol BridgeInterface {
    static func createInstance() -> BridgeInterface
    //func getPythonInformation() -> String
    //func parseData(data :[String])-> (day:[String], hours:[String])
    func login(_ username:String)->String
}

/// A simple class for access to an instance of the python interface
class Bridge {
    static private var instance : BridgeInterface?
    
    static func sharedInstance() -> BridgeInterface {
        return instance!
    }
    static func setSharedInstance(to: BridgeInterface?) {
        instance = to
    }
}
