// Generated by gencpp from file api/MoveGoal.msg
// DO NOT EDIT!


#ifndef API_MESSAGE_MOVEGOAL_H
#define API_MESSAGE_MOVEGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/UInt8.h>

namespace api
{
template <class ContainerAllocator>
struct MoveGoal_
{
  typedef MoveGoal_<ContainerAllocator> Type;

  MoveGoal_()
    : topics()
    , data()  {
    }
  MoveGoal_(const ContainerAllocator& _alloc)
    : topics(_alloc)
    , data(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > , typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::other >  _topics_type;
  _topics_type topics;

   typedef std::vector< ::std_msgs::UInt8_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::std_msgs::UInt8_<ContainerAllocator> >::other >  _data_type;
  _data_type data;





  typedef boost::shared_ptr< ::api::MoveGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::api::MoveGoal_<ContainerAllocator> const> ConstPtr;

}; // struct MoveGoal_

typedef ::api::MoveGoal_<std::allocator<void> > MoveGoal;

typedef boost::shared_ptr< ::api::MoveGoal > MoveGoalPtr;
typedef boost::shared_ptr< ::api::MoveGoal const> MoveGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::api::MoveGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::api::MoveGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::api::MoveGoal_<ContainerAllocator1> & lhs, const ::api::MoveGoal_<ContainerAllocator2> & rhs)
{
  return lhs.topics == rhs.topics &&
    lhs.data == rhs.data;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::api::MoveGoal_<ContainerAllocator1> & lhs, const ::api::MoveGoal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace api

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::api::MoveGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::api::MoveGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::api::MoveGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::api::MoveGoal_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::api::MoveGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::api::MoveGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::api::MoveGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "313097403ccb5a582ce6161a187ee5cb";
  }

  static const char* value(const ::api::MoveGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x313097403ccb5a58ULL;
  static const uint64_t static_value2 = 0x2ce6161a187ee5cbULL;
};

template<class ContainerAllocator>
struct DataType< ::api::MoveGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "api/MoveGoal";
  }

  static const char* value(const ::api::MoveGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::api::MoveGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"#goal definition\n"
"string[] topics\n"
"std_msgs/UInt8[] data\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/UInt8\n"
"uint8 data\n"
;
  }

  static const char* value(const ::api::MoveGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::api::MoveGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.topics);
      stream.next(m.data);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MoveGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::api::MoveGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::api::MoveGoal_<ContainerAllocator>& v)
  {
    s << indent << "topics[]" << std::endl;
    for (size_t i = 0; i < v.topics.size(); ++i)
    {
      s << indent << "  topics[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.topics[i]);
    }
    s << indent << "data[]" << std::endl;
    for (size_t i = 0; i < v.data.size(); ++i)
    {
      s << indent << "  data[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::std_msgs::UInt8_<ContainerAllocator> >::stream(s, indent + "    ", v.data[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // API_MESSAGE_MOVEGOAL_H
