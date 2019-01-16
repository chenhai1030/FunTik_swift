//
//  ViewController.swift
//  FunTik
//
//  Created by chenhai on 2019/1/3.
//  Copyright © 2019 chenhai. All rights reserved.
//

import Cocoa
import Foundation

class ViewController: NSViewController {

    @IBOutlet var LoginView: NSView!
    
    @IBOutlet weak var UserID: NSTextField!
    @IBOutlet weak var Password: NSSecureTextField!
    @IBOutlet weak var SubmitBtn: NSButtonCell!
    
    //let Spider = Bridge.sharedInstance()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        NSApp.activate(ignoringOtherApps: true)
        
        NotificationCenter.default.addObserver(self, selector: #selector(textViewDidChange(notification:)), name: NSTextField.textDidChangeNotification, object: nil)
        // Do any additional setup after loading the view.
    }

    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }
    
    @objc func textViewDidChange(notification: Notification){
        checkUserInput()
    }
    
    func checkUserInput(){
        if (UserID.stringValue.isEmpty || Password.stringValue.isEmpty){
            print("one is empty")
        }
        else{
            SubmitBtn.isEnabled = true
        }
    }
    
    func shakeAnimationForView(){
        let frame = LoginView.frame
        
        let _numberOfShakes = 1...3
        let _durationOfShake = 0.3
        let _vigourOfShake :CGFloat = 0.04
        
        let shakeAnimation = CAKeyframeAnimation.init()
        let shakePath = CGMutablePath()

        let frameOrigin = CGPoint(x:460, y:280)
        shakePath.move(to: CGPoint(x:frameOrigin.x, y:frameOrigin.y))
        for _ in _numberOfShakes{
            shakePath.addLine(to: CGPoint(x:frameOrigin.x - frame.size.width * _vigourOfShake, y:frameOrigin.y))
            shakePath.addLine(to: CGPoint(x:frameOrigin.x + frame.size.width * _vigourOfShake, y:frameOrigin.y))
        }
        shakePath.closeSubpath()
        shakeAnimation.path = shakePath
        shakeAnimation.duration = _durationOfShake

        LoginView.window?.animations = ["frameOrigin": shakeAnimation]
        LoginView.window?.animator().setFrameOrigin(frameOrigin)
    }

    @IBAction func quitClicked(sender: NSViewController) {
        NSApplication.shared.terminate(self)
    }
    
    @IBAction func Submit(_ sender: NSButton) {
//        let storyboard = NSStoryboard(name: "Main", bundle: nil)
        let username = UserID.stringValue
//        let password = Password.stringValue
        
        let ret = Bridge.sharedInstance().login(username)
        print("chenhai " + ret)
        if (ret != "1")
        {
            shakeAnimationForView()
        }
    }
    
}

