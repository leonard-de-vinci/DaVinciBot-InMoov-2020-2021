;; Auto-generated. Do not edit!


(when (boundp 'api::MoveFeedback)
  (if (not (find-package "API"))
    (make-package "API"))
  (shadow 'MoveFeedback (find-package "API")))
(unless (find-package "API::MOVEFEEDBACK")
  (make-package "API::MOVEFEEDBACK"))

(in-package "ROS")
;;//! \htmlinclude MoveFeedback.msg.html


(defclass api::MoveFeedback
  :super ros::object
  :slots (_progress ))

(defmethod api::MoveFeedback
  (:init
   (&key
    ((:progress __progress) 0)
    )
   (send-super :init)
   (setq _progress (round __progress))
   self)
  (:progress
   (&optional __progress)
   (if __progress (setq _progress __progress)) _progress)
  (:serialization-length
   ()
   (+
    ;; uint8 _progress
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _progress
       (write-byte _progress s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _progress
     (setq _progress (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get api::MoveFeedback :md5sum-) "d0ccee79f15d1d61b42a87d5f604edbc")
(setf (get api::MoveFeedback :datatype-) "api/MoveFeedback")
(setf (get api::MoveFeedback :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#feedback
uint8 progress


")



(provide :api/MoveFeedback "d0ccee79f15d1d61b42a87d5f604edbc")


