; Auto-generated. Do not edit!


(cl:in-package api-msg)


;//! \htmlinclude moveFeedback.msg.html

(cl:defclass <moveFeedback> (roslisp-msg-protocol:ros-message)
  ((feedback
    :reader feedback
    :initarg :feedback
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass moveFeedback (<moveFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <moveFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'moveFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name api-msg:<moveFeedback> is deprecated: use api-msg:moveFeedback instead.")))

(cl:ensure-generic-function 'feedback-val :lambda-list '(m))
(cl:defmethod feedback-val ((m <moveFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader api-msg:feedback-val is deprecated.  Use api-msg:feedback instead.")
  (feedback m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <moveFeedback>) ostream)
  "Serializes a message object of type '<moveFeedback>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'feedback) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <moveFeedback>) istream)
  "Deserializes a message object of type '<moveFeedback>"
    (cl:setf (cl:slot-value msg 'feedback) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<moveFeedback>)))
  "Returns string type for a message object of type '<moveFeedback>"
  "api/moveFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'moveFeedback)))
  "Returns string type for a message object of type 'moveFeedback"
  "api/moveFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<moveFeedback>)))
  "Returns md5sum for a message object of type '<moveFeedback>"
  "f1f168a39479bedb24dba7a087426182")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'moveFeedback)))
  "Returns md5sum for a message object of type 'moveFeedback"
  "f1f168a39479bedb24dba7a087426182")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<moveFeedback>)))
  "Returns full string definition for message of type '<moveFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#feedback~%bool feedback~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'moveFeedback)))
  "Returns full string definition for message of type 'moveFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#feedback~%bool feedback~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <moveFeedback>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <moveFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'moveFeedback
    (cl:cons ':feedback (feedback msg))
))
