// Generated by gencpp from file api/MoveActionGoal.msg
// DO NOT EDIT!


#ifndef API_MESSAGE_MOVEACTIONGOAL_H
#define API_MESSAGE_MOVEACTIONGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <actionlib_msgs/GoalID.h>
#include <api/MoveGoal.h>

namespace api
{
template <class ContainerAllocator>
struct MoveActionGoal_
{
  typedef MoveActionGoal_<ContainerAllocator> Type;

  MoveActionGoal_()
    : header()
    , goal_id()
    , goal()  {
    }
  MoveActionGoal_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , goal_id(_alloc)
    , goal(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef  ::actionlib_msgs::GoalID_<ContainerAllocator>  _goal_id_type;
  _goal_id_type goal_id;

   typedef  ::api::MoveGoal_<ContainerAllocator>  _goal_type;
  _goal_type goal;





  typedef boost::shared_ptr< ::api::MoveActionGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::api::MoveActionGoal_<ContainerAllocator> const> ConstPtr;

}; // struct MoveActionGoal_

typedef ::api::MoveActionGoal_<std::allocator<void> > MoveActionGoal;

typedef boost::shared_ptr< ::api::MoveActionGoal > MoveActionGoalPtr;
typedef boost::shared_ptr< ::api::MoveActionGoal const> MoveActionGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::api::MoveActionGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::api::MoveActionGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::api::MoveActionGoal_<ContainerAllocator1> & lhs, const ::api::MoveActionGoal_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.goal_id == rhs.goal_id &&
    lhs.goal == rhs.goal;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::api::MoveActionGoal_<ContainerAllocator1> & lhs, const ::api::MoveActionGoal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace api

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::api::MoveActionGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::api::MoveActionGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::api::MoveActionGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::api::MoveActionGoal_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::api::MoveActionGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::api::MoveActionGoal_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::api::MoveActionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "8dce3c059b0f08e28a507d9930e6242e";
  }

  static const char* value(const ::api::MoveActionGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x8dce3c059b0f08e2ULL;
  static const uint64_t static_value2 = 0x8a507d9930e6242eULL;
};

template<class ContainerAllocator>
struct DataType< ::api::MoveActionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "api/MoveActionGoal";
  }

  static const char* value(const ::api::MoveActionGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::api::MoveActionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"\n"
"Header header\n"
"actionlib_msgs/GoalID goal_id\n"
"MoveGoal goal\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: actionlib_msgs/GoalID\n"
"# The stamp should store the time at which this goal was requested.\n"
"# It is used by an action server when it tries to preempt all\n"
"# goals that were requested before a certain time\n"
"time stamp\n"
"\n"
"# The id provides a way to associate feedback and\n"
"# result message with specific goal requests. The id\n"
"# specified must be unique.\n"
"string id\n"
"\n"
"\n"
"================================================================================\n"
"MSG: api/MoveGoal\n"
"# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"#goal definition\n"
"string[] topics\n"
"std_msgs/UInt8[] data\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/UInt8\n"
"uint8 data\n"
;
  }

  static const char* value(const ::api::MoveActionGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::api::MoveActionGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.goal_id);
      stream.next(m.goal);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MoveActionGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::api::MoveActionGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::api::MoveActionGoal_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "goal_id: ";
    s << std::endl;
    Printer< ::actionlib_msgs::GoalID_<ContainerAllocator> >::stream(s, indent + "  ", v.goal_id);
    s << indent << "goal: ";
    s << std::endl;
    Printer< ::api::MoveGoal_<ContainerAllocator> >::stream(s, indent + "  ", v.goal);
  }
};

} // namespace message_operations
} // namespace ros

#endif // API_MESSAGE_MOVEACTIONGOAL_H
