; Auto-generated. Do not edit!


(cl:in-package api-msg)


;//! \htmlinclude MoveFeedback.msg.html

(cl:defclass <MoveFeedback> (roslisp-msg-protocol:ros-message)
  ((progress
    :reader progress
    :initarg :progress
    :type cl:fixnum
    :initform 0))
)

(cl:defclass MoveFeedback (<MoveFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MoveFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MoveFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name api-msg:<MoveFeedback> is deprecated: use api-msg:MoveFeedback instead.")))

(cl:ensure-generic-function 'progress-val :lambda-list '(m))
(cl:defmethod progress-val ((m <MoveFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader api-msg:progress-val is deprecated.  Use api-msg:progress instead.")
  (progress m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MoveFeedback>) ostream)
  "Serializes a message object of type '<MoveFeedback>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'progress)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MoveFeedback>) istream)
  "Deserializes a message object of type '<MoveFeedback>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'progress)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MoveFeedback>)))
  "Returns string type for a message object of type '<MoveFeedback>"
  "api/MoveFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveFeedback)))
  "Returns string type for a message object of type 'MoveFeedback"
  "api/MoveFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MoveFeedback>)))
  "Returns md5sum for a message object of type '<MoveFeedback>"
  "d0ccee79f15d1d61b42a87d5f604edbc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MoveFeedback)))
  "Returns md5sum for a message object of type 'MoveFeedback"
  "d0ccee79f15d1d61b42a87d5f604edbc")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MoveFeedback>)))
  "Returns full string definition for message of type '<MoveFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#feedback~%uint8 progress~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MoveFeedback)))
  "Returns full string definition for message of type 'MoveFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#feedback~%uint8 progress~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MoveFeedback>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MoveFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'MoveFeedback
    (cl:cons ':progress (progress msg))
))
