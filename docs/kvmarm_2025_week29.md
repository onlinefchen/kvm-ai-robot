# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 10:11:47

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 274
- **总 Thread 数**: 24
- **大型 Thread** (>20封): 5 个

### 分类分布

- **PATCH**: 21 threads (266 邮件)
- **GIT PULL**: 2 threads (5 邮件)
- **Other**: 1 threads (3 邮件)

---

## 📌 PATCH

共 21 个 thread

---

### Thread 1: [PATCH v14 00/21] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs

**📧 邮件数**: 59 | **👥 参与者**: 5 | **📅 开始时间**: Tue, 15 Jul 2025 10:33:29 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个名为“[PATCH v14 00/21] KVM: Enable host userspace mapping for guest_memfd-backed memory for non-CoCo VMs”的补丁系列，旨在为非CoCo虚拟机启用主机用户空间映射功能，以支持基于guest_memfd的内存。

**补丁内容**：
该补丁系列的主要目标是允许虚拟机监控器（VMM）如Firecracker完全使用guest_memfd支持的内存，从而简化内存管理模型并提高安全性。补丁分为多个部分，包括基础设施重构、对x86和arm64的支持、引入新的KVM能力标志等。

**历史讨论要点**：
在之前的讨论中，补丁的设计和实现细节得到了广泛的反馈，包括对KVM配置选项的重命名（如将CONFIG_KVM_PRIVATE_MEM重命名为CONFIG_KVM_GMEM），以及对guest_memfd支持的清晰化。

**本周新讨论及进展**：
本周的讨论集中在补丁的具体实现和命名上，参与者对补丁的各个部分进行了审查和反馈。特别是，补丁引入了新的KVM能力KVM_CAP_GMEM_MMAP，允许用户空间映射guest_memfd支持的内存。此外，补丁还扩展了自测试，以确保在支持mmap的情况下，guest_memfd的功能正常。参与者对补丁的命名和逻辑进行了深入讨论，确保其符合KVM的整体设计目标。

总的来说，这一系列补丁的实施将为KVM提供更强大的内存管理能力，并增强其在虚拟化环境中的安全性和灵活性。

#### 📝 邮件列表

1. **[07-15 10:33]** [PATCH v14 00/21] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[07-15 10:33]** [PATCH v14 01/21] KVM: Rename CONFIG_KVM_PRIVATE_MEM to CONFIG_KVM_GMEM
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[07-15 10:33]** [PATCH v14 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[07-15 10:33]** [PATCH v14 03/21] KVM: Introduce kvm_arch_supports_gmem()
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[07-15 10:33]** [PATCH v14 04/21] KVM: x86: Introduce kvm->arch.supports_gmem
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[07-15 10:33]** [PATCH v14 05/21] KVM: Rename kvm_slot_can_be_private() to kvm_slot_has_gmem()
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[07-15 10:33]** [PATCH v14 06/21] KVM: Fix comments that refer to slots_lock
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[07-15 10:33]** [PATCH v14 07/21] KVM: Fix comment that refers to kvm uapi header path
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[07-15 10:33]** [PATCH v14 08/21] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[07-15 10:33]** [PATCH v14 09/21] KVM: guest_memfd: Track guest_memfd mmap support in memslot
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[07-15 10:33]** [PATCH v14 10/21] KVM: x86/mmu: Generalize private_max_mapping_level
 x86 op to max_mapping_level
   - 发件人: Fuad Tabba <tabba@google.com>
12. **[07-15 10:33]** [PATCH v14 11/21] KVM: x86/mmu: Allow NULL-able fault in kvm_max_private_mapping_level
   - 发件人: Fuad Tabba <tabba@google.com>
13. **[07-15 10:33]** [PATCH v14 12/21] KVM: x86/mmu: Consult guest_memfd when computing max_mapping_level
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[07-15 10:33]** [PATCH v14 13/21] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Fuad Tabba <tabba@google.com>
15. **[07-15 10:33]** [PATCH v14 14/21] KVM: x86: Enable guest_memfd mmap for default VM type
   - 发件人: Fuad Tabba <tabba@google.com>
16. **[07-15 10:33]** [PATCH v14 15/21] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
17. **[07-15 10:33]** [PATCH v14 16/21] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Fuad Tabba <tabba@google.com>
18. **[07-15 10:33]** [PATCH v14 17/21] KVM: arm64: nv: Handle VNCR_EL2-triggered faults
 backed by guest_memfd
   - 发件人: Fuad Tabba <tabba@google.com>
19. **[07-15 10:33]** [PATCH v14 18/21] KVM: arm64: Enable host mapping of shared
 guest_memfd memory
   - 发件人: Fuad Tabba <tabba@google.com>
20. **[07-15 10:33]** [PATCH v14 19/21] KVM: Introduce the KVM capability KVM_CAP_GMEM_MMAP
   - 发件人: Fuad Tabba <tabba@google.com>
21. **[07-15 10:33]** [PATCH v14 20/21] KVM: selftests: Do not use hardcoded page sizes in
 guest_memfd test
   - 发件人: Fuad Tabba <tabba@google.com>
22. **[07-15 10:33]** [PATCH v14 21/21] KVM: selftests: guest_memfd mmap() test when mmap
 is supported
   - 发件人: Fuad Tabba <tabba@google.com>
23. **[07-16 11:43]** Re: [PATCH v14 01/21] KVM: Rename CONFIG_KVM_PRIVATE_MEM to
 CONFIG_KVM_GMEM
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
24. **[07-16 12:08]** Re: [PATCH v14 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to
 CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
25. **[07-16 13:07]** Re: [PATCH v14 03/21] KVM: Introduce kvm_arch_supports_gmem()
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
26. **[07-16 13:18]** Re: [PATCH v14 04/21] KVM: x86: Introduce kvm->arch.supports_gmem
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
27. **[07-16 13:19]** Re: [PATCH v14 05/21] KVM: Rename kvm_slot_can_be_private() to
 kvm_slot_has_gmem()
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
28. **[07-16 13:20]** Re: [PATCH v14 06/21] KVM: Fix comments that refer to slots_lock
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
29. **[07-16 13:24]** Re: [PATCH v14 07/21] KVM: Fix comment that refers to kvm uapi header
 path
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
30. **[07-16 13:40]** Re: [PATCH v14 08/21] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
31. **[07-16 14:10]** Re: [PATCH v14 09/21] KVM: guest_memfd: Track guest_memfd mmap
 support in memslot
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
32. **[07-16 09:11]** Re: [PATCH v14 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Fuad Tabba <tabba@google.com>
33. **[07-16 09:15]** Re: [PATCH v14 08/21] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Fuad Tabba <tabba@google.com>
34. **[07-16 09:21]** Re: [PATCH v14 09/21] KVM: guest_memfd: Track guest_memfd mmap
 support in memslot
   - 发件人: Fuad Tabba <tabba@google.com>
35. **[07-16 16:31]** Re: [PATCH v14 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to
 CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
36. **[07-16 16:52]** Re: [PATCH v14 09/21] KVM: guest_memfd: Track guest_memfd mmap
 support in memslot
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
37. **[07-16 12:25]** Re: [PATCH v14 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to
 CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: David Hildenbrand <david@redhat.com>
38. **[07-16 12:31]** Re: [PATCH v14 09/21] KVM: guest_memfd: Track guest_memfd mmap
 support in memslot
   - 发件人: David Hildenbrand <david@redhat.com>
39. **[07-16 12:32]** Re: [PATCH v14 14/21] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: David Hildenbrand <david@redhat.com>
40. **[07-16 12:36]** Re: [PATCH v14 15/21] KVM: arm64: Refactor user_mem_abort()
   - 发件人: David Hildenbrand <david@redhat.com>
41. **[07-16 11:59]** Re: [PATCH v14 09/21] KVM: guest_memfd: Track guest_memfd mmap
 support in memslot
   - 发件人: Fuad Tabba <tabba@google.com>
42. **[07-16 19:02]** Re: [PATCH v14 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to
 CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
43. **[07-16 12:05]** Re: [PATCH v14 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Fuad Tabba <tabba@google.com>
44. **[07-16 13:15]** Re: [PATCH v14 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to
 CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: David Hildenbrand <david@redhat.com>
45. **[07-16 12:26]** Re: [PATCH v14 15/21] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
46. **[07-16 20:01]** Re: [PATCH v14 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to
 CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
47. **[07-16 13:13]** Re: [PATCH v14 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Fuad Tabba <tabba@google.com>
48. **[07-16 14:14]** Re: [PATCH v14 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to
 CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: David Hildenbrand <david@redhat.com>
49. **[07-16 13:24]** Re: [PATCH v14 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Fuad Tabba <tabba@google.com>
50. **[07-16 20:39]** Re: [PATCH v14 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to
 CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
51. **[07-16 13:54]** Re: [PATCH v14 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Fuad Tabba <tabba@google.com>
52. **[07-16 14:59]** Re: [PATCH v14 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to
 CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: David Hildenbrand <david@redhat.com>
53. **[07-16 16:08]** Re: [PATCH v14 15/21] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Marc Zyngier <maz@kernel.org>
54. **[07-16 17:12]** Re: [PATCH v14 04/21] KVM: x86: Introduce kvm->arch.supports_gmem
   - 发件人: Ackerley Tng <ackerleytng@google.com>
55. **[07-17 09:48]** Re: [PATCH v14 04/21] KVM: x86: Introduce kvm->arch.supports_gmem
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
56. **[07-17 09:49]** Re: [PATCH v14 04/21] KVM: x86: Introduce kvm->arch.supports_gmem
   - 发件人: Fuad Tabba <tabba@google.com>
57. **[07-17 17:00]** Re: [PATCH v14 04/21] KVM: x86: Introduce kvm->arch.supports_gmem
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
58. **[07-17 09:50]** Re: [PATCH v14 04/21] KVM: x86: Introduce kvm->arch.supports_gmem
   - 发件人: Ackerley Tng <ackerleytng@google.com>
59. **[07-17 17:59]** Re: [PATCH v14 04/21] KVM: x86: Introduce kvm->arch.supports_gmem
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 2: [PATCH v15 00/21] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs

**📧 邮件数**: 32 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 17 Jul 2025 17:27:10 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于KVM（Kernel-based Virtual Machine）的补丁系列，主要内容是启用主机用户空间映射支持，针对使用`guest_memfd`作为内存后端的非CoCo虚拟机。以下是总结：

1. **原始补丁内容**：补丁系列的核心是使KVM能够支持主机用户空间映射`guest_memfd`背后的内存，这对于多种KVM用例至关重要，例如允许VMM（虚拟机监控器）如Firecracker完全基于`guest_memfd`运行虚拟机。

2. **历史讨论要点**：之前的讨论集中在补丁的结构和功能上，包括基础设施重构、对`guest_memfd`的支持以及如何处理内存映射和故障处理。补丁还强调了安全性增强，通过消除主机内核对虚拟机内存的直接映射来防止潜在的攻击。

3. **本周新讨论与进展**：本周的讨论主要集中在补丁的具体实现和审查反馈上。参与者对补丁的不同部分进行了审查和讨论，提出了对代码注释、函数命名和逻辑清晰度的建议。特别是，补丁引入了新的KVM能力`KVM_CAP_GMEM_MMAP`，以指示支持`guest_memfd`的主机用户空间映射。此外，补丁还扩展了自测功能，确保在不同VM类型下的`guest_memfd`映射功能正常。

总的来说，本周的讨论推动了补丁的进展，参与者对补丁的整体功能表示认可，并计划在QEMU中进行POC（概念验证）测试，以确保非CoCo虚拟机的`guest_memfd`支持正常工作。

#### 📝 邮件列表

1. **[07-17 17:27]** [PATCH v15 00/21] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[07-17 17:27]** [PATCH v15 01/21] KVM: Rename CONFIG_KVM_PRIVATE_MEM to CONFIG_KVM_GMEM
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[07-17 17:27]** [PATCH v15 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[07-17 17:27]** [PATCH v15 03/21] KVM: Introduce kvm_arch_supports_gmem()
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[07-17 17:27]** [PATCH v15 04/21] KVM: x86: Introduce kvm->arch.supports_gmem
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[07-17 17:27]** [PATCH v15 05/21] KVM: Rename kvm_slot_can_be_private() to kvm_slot_has_gmem()
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[07-17 17:27]** [PATCH v15 06/21] KVM: Fix comments that refer to slots_lock
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[07-17 17:27]** [PATCH v15 07/21] KVM: Fix comment that refers to kvm uapi header path
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[07-17 17:27]** [PATCH v15 08/21] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[07-17 17:27]** [PATCH v15 09/21] KVM: guest_memfd: Track guest_memfd mmap support in memslot
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[07-17 17:27]** [PATCH v15 10/21] KVM: x86/mmu: Generalize private_max_mapping_level
 x86 op to max_mapping_level
   - 发件人: Fuad Tabba <tabba@google.com>
12. **[07-17 17:27]** [PATCH v15 11/21] KVM: x86/mmu: Allow NULL-able fault in kvm_max_private_mapping_level
   - 发件人: Fuad Tabba <tabba@google.com>
13. **[07-17 17:27]** [PATCH v15 12/21] KVM: x86/mmu: Consult guest_memfd when computing max_mapping_level
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[07-17 17:27]** [PATCH v15 13/21] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Fuad Tabba <tabba@google.com>
15. **[07-17 17:27]** [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default VM type
   - 发件人: Fuad Tabba <tabba@google.com>
16. **[07-17 17:27]** [PATCH v15 15/21] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
17. **[07-17 17:27]** [PATCH v15 16/21] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Fuad Tabba <tabba@google.com>
18. **[07-17 17:27]** [PATCH v15 17/21] KVM: arm64: nv: Handle VNCR_EL2-triggered faults
 backed by guest_memfd
   - 发件人: Fuad Tabba <tabba@google.com>
19. **[07-17 17:27]** [PATCH v15 18/21] KVM: arm64: Enable host mapping of shared
 guest_memfd memory
   - 发件人: Fuad Tabba <tabba@google.com>
20. **[07-17 17:27]** [PATCH v15 19/21] KVM: Introduce the KVM capability KVM_CAP_GMEM_MMAP
   - 发件人: Fuad Tabba <tabba@google.com>
21. **[07-17 17:27]** [PATCH v15 20/21] KVM: selftests: Do not use hardcoded page sizes in
 guest_memfd test
   - 发件人: Fuad Tabba <tabba@google.com>
22. **[07-17 17:27]** [PATCH v15 21/21] KVM: selftests: guest_memfd mmap() test when mmap
 is supported
   - 发件人: Fuad Tabba <tabba@google.com>
23. **[07-18 09:42]** Re: [PATCH v15 03/21] KVM: Introduce kvm_arch_supports_gmem()
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
24. **[07-18 10:56]** Re: [PATCH v15 08/21] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
25. **[07-18 11:33]** Re: [PATCH v15 09/21] KVM: guest_memfd: Track guest_memfd mmap
 support in memslot
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
26. **[07-18 13:10]** Re: [PATCH v15 11/21] KVM: x86/mmu: Allow NULL-able fault in
 kvm_max_private_mapping_level
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
27. **[07-18 13:32]** Re: [PATCH v15 12/21] KVM: x86/mmu: Consult guest_memfd when
 computing max_mapping_level
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
28. **[07-18 13:57]** Re: [PATCH v15 12/21] KVM: x86/mmu: Consult guest_memfd when
 computing max_mapping_level
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
29. **[07-18 14:09]** Re: [PATCH v15 13/21] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
30. **[07-18 14:10]** Re: [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
31. **[07-18 14:14]** Re: [PATCH v15 19/21] KVM: Introduce the KVM capability
 KVM_CAP_GMEM_MMAP
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
32. **[07-18 14:19]** Re: [PATCH v15 10/21] KVM: x86/mmu: Generalize
 private_max_mapping_level x86 op to max_mapping_level
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>

---

### Thread 3: [PATCH v4 00/23] ARM64 PMU Partitioning

**📧 邮件数**: 28 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 14 Jul 2025 22:58:54 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的 PMU（性能监控单元）分区的补丁系列，主要集中在如何优化虚拟化环境中的 PMU 访问。

1. **原始补丁内容**：补丁系列旨在实现 ARM64 的分区 PMU 方案，允许为虚拟机（VM）保留部分计数器，从而减少性能开销。补丁中包括对 PMU 控制寄存器的修改，以及对 KVM（内核虚拟机）的支持。

2. **历史讨论要点**：之前的讨论主要集中在如何有效地管理 PMU 计数器的访问，确保虚拟机能够高效地使用这些资源。讨论中提到，分区 PMU 只在 VHE（虚拟化硬件扩展）模式下支持，并且需要在引导时配置。

3. **本周新讨论和进展**：本周的讨论主要集中在补丁的细节上，包括对 PMU 寄存器的读写处理、IRQ（中断请求）管理、以及如何在分区模式下进行上下文切换。补丁还引入了 ioctl 接口，以便在支持的情况下启用分区 PMU，并增加了自测用例以验证新功能的正确性。此外，针对编译错误和警告的反馈也被提及，开发者表示将进行修正。

总体而言，这一系列补丁旨在提升 ARM64 架构下 KVM 的性能监控能力，确保在虚拟化环境中能够有效利用 PMU 资源。

#### 📝 邮件列表

1. **[07-14 22:58]** [PATCH v4 00/23] ARM64 PMU Partitioning
   - 发件人: Colton Lewis <coltonlewis@google.com>
2. **[07-14 22:58]** [PATCH v4 01/23] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Colton Lewis <coltonlewis@google.com>
3. **[07-14 22:58]** [PATCH v4 02/23] KVM: arm64: Reorganize PMU includes
   - 发件人: Colton Lewis <coltonlewis@google.com>
4. **[07-14 22:58]** [PATCH v4 03/23] KVM: arm64: Reorganize PMU functions
   - 发件人: Colton Lewis <coltonlewis@google.com>
5. **[07-14 22:58]** [PATCH v4 04/23] perf: arm_pmuv3: Introduce method to partition the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
6. **[07-14 22:58]** [PATCH v4 05/23] perf: arm_pmuv3: Generalize counter bitmasks
   - 发件人: Colton Lewis <coltonlewis@google.com>
7. **[07-14 22:59]** [PATCH v4 06/23] perf: arm_pmuv3: Keep out of guest counter partition
   - 发件人: Colton Lewis <coltonlewis@google.com>
8. **[07-14 22:59]** [PATCH v4 07/23] KVM: arm64: Account for partitioning in kvm_pmu_get_max_counters()
   - 发件人: Colton Lewis <coltonlewis@google.com>
9. **[07-14 22:59]** [PATCH v4 08/23] KVM: arm64: Introduce non-UNDEF FGT control
   - 发件人: Colton Lewis <coltonlewis@google.com>
10. **[07-14 22:59]** [PATCH v4 09/23] KVM: arm64: Set up FGT for Partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
11. **[07-14 22:59]** [PATCH v4 10/23] KVM: arm64: Writethrough trapped PMEVTYPER register
   - 发件人: Colton Lewis <coltonlewis@google.com>
12. **[07-14 22:59]** [PATCH v4 11/23] KVM: arm64: Use physical PMSELR for PMXEVTYPER if partitioned
   - 发件人: Colton Lewis <coltonlewis@google.com>
13. **[07-14 22:59]** [PATCH v4 12/23] KVM: arm64: Writethrough trapped PMOVS register
   - 发件人: Colton Lewis <coltonlewis@google.com>
14. **[07-14 22:59]** [PATCH v4 13/23] KVM: arm64: Write fast path PMU register handlers
   - 发件人: Colton Lewis <coltonlewis@google.com>
15. **[07-14 22:59]** [PATCH v4 14/23] KVM: arm64: Setup MDCR_EL2 to handle a partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
16. **[07-14 22:59]** [PATCH v4 15/23] KVM: arm64: Account for partitioning in PMCR_EL0 access
   - 发件人: Colton Lewis <coltonlewis@google.com>
17. **[07-14 22:59]** [PATCH v4 16/23] KVM: arm64: Context swap Partitioned PMU guest registers
   - 发件人: Colton Lewis <coltonlewis@google.com>
18. **[07-14 22:59]** [PATCH v4 17/23] KVM: arm64: Enforce PMU event filter at vcpu_load()
   - 发件人: Colton Lewis <coltonlewis@google.com>
19. **[07-14 22:59]** [PATCH v4 18/23] KVM: arm64: Extract enum debug_owner to enum vcpu_register_owner
   - 发件人: Colton Lewis <coltonlewis@google.com>
20. **[07-14 22:59]** [PATCH v4 19/23] KVM: arm64: Implement lazy PMU context swaps
   - 发件人: Colton Lewis <coltonlewis@google.com>
21. **[07-14 22:59]** [PATCH v4 20/23] perf: arm_pmuv3: Handle IRQs for Partitioned PMU
 guest counters
   - 发件人: Colton Lewis <coltonlewis@google.com>
22. **[07-14 22:59]** [PATCH v4 21/23] KVM: arm64: Inject recorded guest interrupts
   - 发件人: Colton Lewis <coltonlewis@google.com>
23. **[07-14 22:59]** [PATCH v4 22/23] KVM: arm64: Add ioctl to partition the PMU when supported
   - 发件人: Colton Lewis <coltonlewis@google.com>
24. **[07-14 22:59]** [PATCH v4 23/23] KVM: arm64: selftests: Add test case for partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
25. **[07-16 01:26]** Re: [PATCH v4 22/23] KVM: arm64: Add ioctl to partition the PMU when
 supported
   - 发件人: kernel test robot <lkp@intel.com>
26. **[07-16 01:36]** Re: [PATCH v4 22/23] KVM: arm64: Add ioctl to partition the PMU when
 supported
   - 发件人: kernel test robot <lkp@intel.com>
27. **[07-15 21:16]** Re: [PATCH v4 22/23] KVM: arm64: Add ioctl to partition the PMU when supported
   - 发件人: Colton Lewis <coltonlewis@google.com>
28. **[07-16 00:22]** Re: [PATCH v4 01/23] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>

---

### Thread 4: [PATCH v3 08/10] KVM: arm64: Handle FFA_MEM_LEND calls from the
 host

**📧 邮件数**: 22 | **👥 参与者**: 3 | **📅 开始时间**: Sun, 13 Jul 2025 21:01:12 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理来自主机的 FFA_MEM_LEND 调用的补丁（patch v3 08/10）。该补丁旨在改进 pKVM 对内存管理的支持，尤其是在安全世界与非安全世界之间的内存借用。

在历史讨论中，Will Deacon 指出 pKVM 不使用 FF-A（Firmware Framework for Arm）来管理主机和客体之间的页面所有权，强调 FF-A 仅用于安全世界的内存管理，LEND 事务要求安全世界防止非安全访问，而不是依赖 pKVM 进行解除映射。

本周的新讨论中，DaeRo Lee 质疑 pKVM 是否有政策不使用 FF-A 管理非安全内存，尽管 FF-A 规范支持在非安全虚拟机之间进行内存管理。他询问如何通过 FF-A 从主机向客体借用内存，以及 pKVM 是否能够防止这种情况。Will Deacon 则建议查看代码以了解更多细节，表明对该问题的复杂性和对开发者的警示。

总体来看，讨论围绕 pKVM 的内存管理策略及其与 FF-A 规范的兼容性展开，参与者对如何安全地实现内存借用提出了疑问，并探讨了可能的解决方案。

#### 📝 邮件列表

1. **[07-13 21:01]** Re: [PATCH v3 08/10] KVM: arm64: Handle FFA_MEM_LEND calls from the
 host
   - 发件人: Will Deacon <will@kernel.org>
2. **[07-14 10:49]** Re: [PATCH v3 08/10] KVM: arm64: Handle FFA_MEM_LEND calls from the host
   - 发件人: DaeRo Lee <skseofh@gmail.com>
3. **[07-14 11:14]** Re: [PATCH v3 08/10] KVM: arm64: Handle FFA_MEM_LEND calls from the host
   - 发件人: DaeRo Lee <skseofh@gmail.com>
4. **[07-14 10:58]** Re: [PATCH v3 08/10] KVM: arm64: Handle FFA_MEM_LEND calls from the
 host
   - 发件人: Will Deacon <will@kernel.org>
5. **[07-14 14:26]** Re: [PATCH v3 02/10] perf: arm_spe: Support FEAT_SPEv1p4 filters
   - 发件人: Will Deacon <will@kernel.org>
6. **[07-14 14:32]** Re: [PATCH v3 01/10] arm64: sysreg: Add new PMSFCR_EL1 fields and
 PMSDSFR_EL1 register
   - 发件人: Will Deacon <will@kernel.org>
7. **[07-14 14:46]** Re: [PATCH v3 03/10] perf: arm_spe: Add support for FEAT_SPE_EFT
 extended filtering
   - 发件人: Will Deacon <will@kernel.org>
8. **[07-14 14:54]** Re: [PATCH v3 04/10] arm64/boot: Enable EL2 requirements for
 SPE_FEAT_FDS
   - 发件人: Will Deacon <will@kernel.org>
9. **[07-14 14:56]** Re: [PATCH v3 06/10] perf: Add perf_event_attr::config4
   - 发件人: Will Deacon <will@kernel.org>
10. **[07-14 15:04]** Re: [PATCH v3 07/10] perf: arm_spe: Add support for filtering on
 data source
   - 发件人: Will Deacon <will@kernel.org>
11. **[07-15 12:23]** Re: [PATCH v3 02/10] perf: arm_spe: Support FEAT_SPEv1p4 filters
   - 发件人: James Clark <james.clark@linaro.org>
12. **[07-15 13:39]** Re: [PATCH v3 03/10] perf: arm_spe: Add support for FEAT_SPE_EFT
 extended filtering
   - 发件人: James Clark <james.clark@linaro.org>
13. **[07-15 13:48]** Re: [PATCH v3 04/10] arm64/boot: Enable EL2 requirements for
 SPE_FEAT_FDS
   - 发件人: James Clark <james.clark@linaro.org>
14. **[07-15 13:57]** Re: [PATCH v3 04/10] arm64/boot: Enable EL2 requirements for
 SPE_FEAT_FDS
   - 发件人: Will Deacon <will@kernel.org>
15. **[07-15 14:04]** Re: [PATCH v3 07/10] perf: arm_spe: Add support for filtering on data
 source
   - 发件人: James Clark <james.clark@linaro.org>
16. **[07-15 14:10]** Re: [PATCH v3 04/10] arm64/boot: Enable EL2 requirements for
 SPE_FEAT_FDS
   - 发件人: James Clark <james.clark@linaro.org>
17. **[07-15 14:28]** Re: [PATCH v3 04/10] arm64/boot: Enable EL2 requirements for
 SPE_FEAT_FDS
   - 发件人: James Clark <james.clark@linaro.org>
18. **[07-17 12:52]** Re: [PATCH v3 04/10] arm64/boot: Enable EL2 requirements for
 SPE_FEAT_FDS
   - 发件人: Will Deacon <will@kernel.org>
19. **[07-17 15:29]** Re: [PATCH v3 07/10] perf: arm_spe: Add support for filtering on
 data source
   - 发件人: Will Deacon <will@kernel.org>
20. **[07-17 16:16]** Re: [PATCH v3 07/10] perf: arm_spe: Add support for filtering on data
 source
   - 发件人: James Clark <james.clark@linaro.org>
21. **[07-17 16:27]** Re: [PATCH v3 07/10] perf: arm_spe: Add support for filtering on
 data source
   - 发件人: Will Deacon <will@kernel.org>
22. **[07-17 17:42]** Re: [PATCH v3 07/10] perf: arm_spe: Add support for filtering on data
 source
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 5: [PATCH v3 00/13] stackleak: Support Clang stack depth tracking

**📧 邮件数**: 21 | **👥 参与者**: 7 | **📅 开始时间**: Thu, 17 Jul 2025 16:25:05 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个名为「stackleak」的补丁系列，旨在支持 Clang 的栈深度跟踪功能。该补丁系列的核心是将原有的 stackleak 功能重命名为 KSTACK_ERASE，并通过 Clang 的新特性实现栈深度跟踪，增强内核的安全性。

在历史讨论中，Kees Cook 提出了将 stackleak 功能从 GCC 插件迁移到 Clang 实现的计划，并在补丁中进行了多项重命名和结构调整，以便更好地支持不同架构的编译和链接。

本周的新讨论主要集中在以下几个方面：
1. Kees Cook 提交了多个补丁，分别处理不同架构（如 x86、ARM、s390 和 MIPS）中 KCOV 的 __init 和内联函数不匹配的问题，确保这些函数在编译时能够正确标记。
2. 讨论了如何在 Clang 和 GCC 插件之间实现 KSTACK_ERASE 的支持，确保在系统初始化时能够有效清除栈信息。
3. 参与者对补丁进行了审查和反馈，部分补丁获得了认可，讨论了在不同情况下使用 __always_inline 和 __init 的适用性。

总体来看，本周的讨论推动了 KSTACK_ERASE 功能的进一步完善，确保其在不同架构下的兼容性和稳定性。

#### 📝 邮件列表

1. **[07-17 16:25]** [PATCH v3 00/13] stackleak: Support Clang stack depth tracking
   - 发件人: Kees Cook <kees@kernel.org>
2. **[07-17 16:25]** [PATCH v3 01/13] stackleak: Rename STACKLEAK to KSTACK_ERASE
   - 发件人: Kees Cook <kees@kernel.org>
3. **[07-17 16:25]** [PATCH v3 02/13] stackleak: Rename stackleak_track_stack to __sanitizer_cov_stack_depth
   - 发件人: Kees Cook <kees@kernel.org>
4. **[07-17 16:25]** [PATCH v3 03/13] stackleak: Split KSTACK_ERASE_CFLAGS from GCC_PLUGINS_CFLAGS
   - 发件人: Kees Cook <kees@kernel.org>
5. **[07-17 16:25]** [PATCH v3 04/13] x86: Handle KCOV __init vs inline mismatches
   - 发件人: Kees Cook <kees@kernel.org>
6. **[07-17 16:25]** [PATCH v3 05/13] arm: Handle KCOV __init vs inline mismatches
   - 发件人: Kees Cook <kees@kernel.org>
7. **[07-17 16:25]** [PATCH v3 06/13] arm64: Handle KCOV __init vs inline mismatches
   - 发件人: Kees Cook <kees@kernel.org>
8. **[07-17 16:25]** [PATCH v3 07/13] s390: Handle KCOV __init vs inline mismatches
   - 发件人: Kees Cook <kees@kernel.org>
9. **[07-17 16:25]** [PATCH v3 08/13] powerpc/mm/book3s64: Move kfence and debug_pagealloc related calls to __init section
   - 发件人: Kees Cook <kees@kernel.org>
10. **[07-17 16:25]** [PATCH v3 09/13] mips: Handle KCOV __init vs inline mismatch
   - 发件人: Kees Cook <kees@kernel.org>
11. **[07-17 16:25]** [PATCH v3 10/13] init.h: Disable sanitizer coverage for __init and __head
   - 发件人: Kees Cook <kees@kernel.org>
12. **[07-17 16:25]** [PATCH v3 11/13] kstack_erase: Support Clang stack depth tracking
   - 发件人: Kees Cook <kees@kernel.org>
13. **[07-17 16:25]** [PATCH v3 12/13] configs/hardening: Enable CONFIG_KSTACK_ERASE
   - 发件人: Kees Cook <kees@kernel.org>
14. **[07-17 16:25]** [PATCH v3 13/13] configs/hardening: Enable CONFIG_INIT_ON_FREE_DEFAULT_ON
   - 发件人: Kees Cook <kees@kernel.org>
15. **[07-18 11:36]** Re: [PATCH v3 04/13] x86: Handle KCOV __init vs inline mismatches
   - 发件人: Mike Rapoport <rppt@kernel.org>
16. **[07-18 17:18]** Re: [PATCH v3 09/13] mips: Handle KCOV __init vs inline mismatch
   - 发件人: Huacai Chen <chenhuacai@kernel.org>
17. **[07-18 12:22]** Re: [PATCH v3 06/13] arm64: Handle KCOV __init vs inline mismatches
   - 发件人: Will Deacon <will@kernel.org>
18. **[07-18 07:58]** Re: [PATCH v3 05/13] arm: Handle KCOV __init vs inline mismatches
   - 发件人: Nishanth Menon <nm@ti.com>
19. **[07-18 14:04]** Re: [PATCH v3 05/13] arm: Handle KCOV __init vs inline mismatches
   - 发件人: Lee Jones <lee@kernel.org>
20. **[07-18 15:51]** Re: [PATCH v3 04/13] x86: Handle KCOV __init vs inline mismatches
   - 发件人: Kees Cook <kees@kernel.org>
21. **[07-20 16:10]** Re: [PATCH v3 04/13] x86: Handle KCOV __init vs inline mismatches
   - 发件人: Ard Biesheuvel <ardb@kernel.org>

---

### Thread 6: [PATCH 00/11] KVM: arm64: nv: Userspace register visibility fixes

**📧 邮件数**: 14 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 14 Jul 2025 13:26:23 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的用户空间寄存器可见性修复，涉及 11 个补丁的提交。

**原始补丁内容**：
补丁主要针对 EL2 GICv3 寄存器的可见性问题，指出这些寄存器通过 ONE_REG 接口暴露的方式不一致，且存在一些小问题，如 RVBAR_EL2 不应存在、FEAT_FGT 寄存器的可见性应依赖于特性是否向来宾展示等。

**之前讨论要点**：
在之前的讨论中，参与者指出了当前寄存器暴露方式的不一致性，并提出了需要修复的具体问题。Marc Zyngier 提出了多个修复方案，并请求 Eric 在 QEMU 中进行测试以验证修复效果。

**本周新讨论与进展**：
本周的讨论中，Marc Zyngier 提交了 11 个补丁，涵盖了多个方面的修复和改进，包括：
1. 将 RVBAR_EL2 访问定义为 UNDEF。
2. 隐藏 ICH_*_EL2 寄存器的暴露，直到 GICv3 代码具备必要基础设施。
3. 定义 ICC_SRE_EL2 的常量值，简化代码。
4. 使 GICv3 的保存/恢复过程遵循可见性属性。
5. 通过 KVM_DEV_ARM_VGIC_GRP_CPU_SYSREGS 接口暴露 GICv3 EL2 寄存器。
6. 根据特性可用性条件化 FEAT_FGT 寄存器的暴露，并向用户空间通告 FGT2 寄存器。
7. 更新自测代码以简化寄存器与特性之间的依赖关系，并增加 EL2 寄存器的测试。

经过测试，所有自测均通过，补丁已被应用到下一个开发版本中。

#### 📝 邮件列表

1. **[07-14 13:26]** [PATCH 00/11] KVM: arm64: nv: Userspace register visibility fixes
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-14 13:26]** [PATCH 01/11] KVM: arm64: Make RVBAR_EL2 accesses UNDEF
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[07-14 13:26]** [PATCH 02/11] KVM: arm64: Don't advertise ICH_*_EL2 registers through GET_ONE_REG
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[07-14 13:26]** [PATCH 03/11] KVM: arm64: Define constant value for ICC_SRE_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[07-14 13:26]** [PATCH 04/11] KVM: arm64: Define helper for ICH_VTR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[07-14 13:26]** [PATCH 05/11] KVM: arm64: Let GICv3 save/restore honor visibility attribute
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[07-14 13:26]** [PATCH 06/11] KVM: arm64: Expose GICv3 EL2 registers via KVM_DEV_ARM_VGIC_GRP_CPU_SYSREGS
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[07-14 13:26]** [PATCH 07/11] KVM: arm64: Condition FGT registers on feature availability
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[07-14 13:26]** [PATCH 08/11] KVM: arm64: Advertise FGT2 registers to userspace
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[07-14 13:26]** [PATCH 09/11] KVM: arm64: selftests: get-reg-list: Simplify feature dependency
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[07-14 13:26]** [PATCH 10/11] KVM: arm64: selftests: get-reg-list: Add base EL2 registers
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[07-14 13:26]** [PATCH 11/11] KVM: arm64: Document registers exposed via KVM_DEV_ARM_VGIC_GRP_CPU_SYSREGS
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[07-15 07:49]** Re: [PATCH 09/11] KVM: arm64: selftests: get-reg-list: Simplify
 feature dependency
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>
14. **[07-16 09:47]** Re: [PATCH 00/11] KVM: arm64: nv: Userspace register visibility fixes
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 7: [PATCH v4 0/6] KVM: arm64: Allow userspace to write GICD_TYPER2.nASSGIcap

**📧 邮件数**: 14 | **👥 参与者**: 2 | **📅 开始时间**: Wed,  9 Jul 2025 14:14:11 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下允许用户空间写入 GICD_TYPER2.nASSGIcap 的补丁系列（PATCH v4 0/6）。该补丁旨在允许用户在初始化 VGIC（虚拟通用中断控制器）之前修改 GICD_TYPER2 寄存器的值，以支持虚拟化环境中的特性配置。

在历史讨论中，Oliver Upton 提出了多个补丁，涉及对 VGIC 的不同方面进行改进，包括对 vSGIs（虚拟共享中断）和 vLPIs（虚拟本地中断）的支持、对 GICD_IIDR 寄存器的访问控制等。这些补丁的目标是增强 KVM 的灵活性和兼容性，特别是在处理不同版本的 GIC 时。

在本周的新讨论中，Eric Auger 对多个补丁进行了审查，提出了一些建议和问题，主要集中在补丁的描述和代码逻辑的清晰度上。他对补丁的多个部分表示支持，并给予了“Reviewed-by”标记，表明他认为这些补丁是可接受的。总体而言，本周的讨论主要是对补丁的细节进行审查和确认，没有提出重大的反对意见或新问题。

#### 📝 邮件列表

1. **[07-09 14:14]** [PATCH v4 0/6] KVM: arm64: Allow userspace to write GICD_TYPER2.nASSGIcap
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-09 14:14]** [PATCH v4 1/6] KVM: arm64: Disambiguate support for vSGIs v. vLPIs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[07-09 14:14]** [PATCH v4 2/6] KVM: arm64: vgic-v3: Consolidate MAINT_IRQ handling
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[07-09 14:14]** [PATCH v4 3/6] KVM: arm64: vgic-v3: Allow access to GICD_IIDR prior to initialization
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[07-09 14:14]** [PATCH v4 4/6] KVM: arm64: vgic-v3: Allow userspace to write GICD_TYPER2.nASSGIcap
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[07-09 14:14]** [PATCH v4 5/6] KVM: arm64: selftests: Add test for nASSGIcap attribute
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[07-09 14:14]** [PATCH v4 6/6] Documentation: KVM: arm64: Describe VGICv3 registers writable pre-init
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[07-14 12:20]** Re: [PATCH v4 1/6] KVM: arm64: Disambiguate support for vSGIs v.
 vLPIs
   - 发件人: Eric Auger <eauger@redhat.com>
9. **[07-14 14:52]** Re: [PATCH v4 2/6] KVM: arm64: vgic-v3: Consolidate MAINT_IRQ
 handling
   - 发件人: Eric Auger <eauger@redhat.com>
10. **[07-14 14:59]** Re: [PATCH v4 2/6] KVM: arm64: vgic-v3: Consolidate MAINT_IRQ
 handling
   - 发件人: Eric Auger <eauger@redhat.com>
11. **[07-14 16:41]** Re: [PATCH v4 3/6] KVM: arm64: vgic-v3: Allow access to GICD_IIDR
 prior to initialization
   - 发件人: Eric Auger <eauger@redhat.com>
12. **[07-14 16:58]** Re: [PATCH v4 4/6] KVM: arm64: vgic-v3: Allow userspace to write
 GICD_TYPER2.nASSGIcap
   - 发件人: Eric Auger <eauger@redhat.com>
13. **[07-14 17:03]** Re: [PATCH v4 5/6] KVM: arm64: selftests: Add test for nASSGIcap
 attribute
   - 发件人: Eric Auger <eauger@redhat.com>
14. **[07-14 17:06]** Re: [PATCH v4 6/6] Documentation: KVM: arm64: Describe VGICv3
 registers writable pre-init
   - 发件人: Eric Auger <eauger@redhat.com>

---

### Thread 8: [PATCH v7 0/5] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI

**📧 邮件数**: 10 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 01 Jul 2025 22:06:33 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上支持 FF-A 1.2 及其新的 SEND_DIRECT2 ABI 的一系列补丁（patch）。原始补丁集包含五个部分，旨在确保主机不使用低于已与虚拟机监控器（hypervisor）协商的 FF-A 版本，以解决兼容性问题。

在历史讨论中，参与者 Per Larsen 提出了补丁的必要性，并详细描述了 FF-A 1.2 规范的变化，包括对 SMCCC（Secure Monitor Call Convention）版本的更新以及新消息接口的支持。Marc Zyngier 对补丁中的某些实现细节提出了质疑，认为在处理寄存器时的更改可能存在问题，需确保遵循规范。

在本周的新讨论中，Will Deacon 对补丁集的结构提出了建议，认为应将较大的补丁拆分为更小的独立部分，以便更清晰地处理每项功能。此外，他指出某些检查可能是不必要的，建议简化代码逻辑。Per Larsen 对 Will 的反馈表示认可，并确认即将发布的 v8 版本将解决这些问题。

总体而言，本周的讨论集中在补丁的结构优化和实现细节的澄清上，推动了对 FF-A 1.2 支持的进一步完善。

#### 📝 邮件列表

1. **[07-01 22:06]** [PATCH v7 0/5] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[07-01 22:06]** [PATCH v7 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[07-01 22:06]** [PATCH v7 4/5] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
4. **[07-01 22:06]** [PATCH v7 5/5] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
5. **[07-03 13:38]** Re: [PATCH v7 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization and in host handler
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[07-07 17:06]** Re: [PATCH v7 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen <perl@immunant.com>
7. **[07-18 14:37]** Re: [PATCH v7 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Will Deacon <will@kernel.org>
8. **[07-18 14:45]** Re: [PATCH v7 4/5] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Will Deacon <will@kernel.org>
9. **[07-18 14:53]** Re: [PATCH v7 5/5] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Will Deacon <will@kernel.org>
10. **[07-18 22:54]** Re: [PATCH v7 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen <perl@immunant.com>

---

### Thread 9: [PATCH v13 00/20] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs

**📧 邮件数**: 10 | **👥 参与者**: 3 | **📅 开始时间**: Wed,  9 Jul 2025 11:59:26 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个名为“[PATCH v13 00/20] KVM: Enable host userspace mapping for guest_memfd-backed memory for non-CoCo VMs”的补丁系列，主要目的是为非CoCo虚拟机启用主机用户空间映射支持，特别是针对由guest_memfd支持的内存。这一补丁的实现将简化虚拟机管理程序（VMM）的设计，允许如Firecracker等VMM完全使用guest_memfd支持的内存。

在历史讨论中，参与者们探讨了补丁的具体实现细节，特别是如何处理由guest_memfd支持的内存页故障。Fuad Tabba提出了一个新函数gmem_abort()来处理这些故障，并讨论了在故障处理过程中可能出现的竞争条件，尤其是在内存无效化的情况下。

本周的新讨论中，Fuad和Marc Zyngier确认了补丁中的一些逻辑，并讨论了如何处理潜在的警告机制。Marc提到将使用VM_WARN_ON_ONCE()替代即将废弃的VM_BUG_ON()，并得到了Fuad的认可。整体来看，讨论氛围积极，参与者们对补丁的方向和实现细节达成了一致。

#### 📝 邮件列表

1. **[07-09 11:59]** [PATCH v13 00/20] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[07-09 11:59]** [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[07-11 09:59]** Re: [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest
 page faults
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
4. **[07-11 14:49]** Re: [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[07-11 15:17]** Re: [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest
 page faults
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[07-11 16:48]** Re: [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[07-11 17:37]** Re: [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[07-14 07:35]** Re: [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest
 page faults
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[07-14 08:42]** Re: [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest
 page faults
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[07-14 09:04]** Re: [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 10: [PATCH v8 0/7] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI

**📧 邮件数**: 8 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 19 Jul 2025 02:11:22 +0000

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上对 FF-A（Firmware Framework for Arm）1.2 及 SEND_DIRECT2 ABI 的支持，包含了一个总共七个补丁的系列。

**原始补丁内容**：
补丁集的主要目标是实现对 FF-A 1.2 规范的支持，特别是新的 SEND_DIRECT2 ABI。此 ABI 允许使用 x4-x17 寄存器作为消息负载，并确保主机不使用比与虚拟机管理程序（hypervisor）协商的低版本 FF-A。

**历史讨论要点**：
在之前的讨论中，补丁集经历了多次版本迭代，主要集中在如何正确实现 FF-A 1.2 的接口，确保与现有版本的兼容性，以及更新相关的 SMC（Secure Monitor Call）调用以支持更多参数的传递。

**本周的新讨论与进展**：
1. 本周的讨论中，补丁集的每个补丁都得到了详细的描述和更新，包括对 FF-A 1.2 接口的支持、对不支持的接口的标记，以及对 FF-A 版本的提升。
2. 具体补丁包括修正主机版本降级尝试的返回值、使用 SMCCC 1.2 进行 FF-A 初始化、标记不支持的 FFA_NOTIFICATION_* 调用、更新对 FF-A 1.2 接口的支持状态等。
3. 通过在 QEMU 上测试 Android 启动并加载 Trusty 作为来宾虚拟机，验证了 SEND_DIRECT2 ABI 的成功使用。

整体来看，本周的讨论集中在确保补丁的正确性和兼容性上，为实现 FF-A 1.2 的完整支持奠定了基础。

#### 📝 邮件列表

1. **[07-19 02:11]** [PATCH v8 0/7] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[07-19 02:11]** [PATCH v8 1/7] KVM: arm64: Correct return value on host version
 downgrade attempt
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[07-19 02:11]** [PATCH v8 2/7] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
4. **[07-19 02:11]** [PATCH v8 3/7] KVM: arm64: Mark FFA_NOTIFICATION_* calls as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
5. **[07-19 02:11]** [PATCH v8 4/7] KVM: arm64: Mark optional FF-A 1.2 interfaces as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
6. **[07-19 02:11]** [PATCH v8 5/7] KVM: arm64: Mask response to FFA_FEATURE call
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
7. **[07-19 02:11]** [PATCH v8 6/7] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
8. **[07-19 02:11]** [PATCH v8 7/7] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>

---

### Thread 11: [PATCH 0/2] Dump instructions on panic for pKVM/nvhe

**📧 邮件数**: 8 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 17 Jul 2025 23:47:42 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM 和 nvhe 的内核补丁，主要目的是在系统崩溃时能够转储故障指令，以便于调试内存损坏问题。

**原始补丁内容**：
Mostafa Saleh 提出了两个补丁，第一部分补丁实现了在 nvhe 模式下的崩溃时转储指令，第二部分则为 pKVM 提供类似支持。补丁内容包括将 hypervisor 代码段映射为只读（RO），并在崩溃时转储故障指令。

**之前讨论要点**：
在历史讨论中，参与者们探讨了如何在崩溃时有效地获取和转储指令。Mostafa 解释了在 pKVM 中，hypervisor 代码段的映射方式与 nvhe 不同，因此需要分开处理。同时，讨论中提到了一种替代方案，即让 hypervisor 在崩溃时读取指令并传递给内核处理，但由于寄存器不足，这种方案并不理想。

**本周新讨论与进展**：
本周的讨论集中在补丁的具体实现上。Mostafa 提到，转储指令的功能不再依赖于 `CONFIG_NVHE_EL2_DEBUG`，并且有建议将两个补丁合并以简化处理。Ben Horgan 对此表示理解，并确认补丁的拆分是合理的。整体来看，讨论进展顺利，参与者对补丁的方向表示支持，且没有强烈的异议。

#### 📝 邮件列表

1. **[07-17 23:47]** [PATCH 0/2] Dump instructions on panic for pKVM/nvhe
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[07-17 23:47]** [PATCH 1/2] KVM: arm64: Dump instruction on hyp panic
   - 发件人: Mostafa Saleh <smostafa@google.com>
3. **[07-17 23:47]** [PATCH 2/2] KVM: arm64: Map hyp text as RO and dump instr on panic
   - 发件人: Mostafa Saleh <smostafa@google.com>
4. **[07-18 01:50]** [resend][PATCH 1/2] arm64: kvm: sys_regs: use string choices helper
   - 发件人: Kuninori Morimoto <kuninori.morimoto.gx@renesas.com>
5. **[07-18 01:50]** [resend][PATCH 2/2] arm64: kvm: trace_handle_exit: use string choices helper
   - 发件人: Kuninori Morimoto <kuninori.morimoto.gx@renesas.com>
6. **[07-18 11:16]** Re: [PATCH 2/2] KVM: arm64: Map hyp text as RO and dump instr on
 panic
   - 发件人: Ben Horgan <ben.horgan@arm.com>
7. **[07-18 10:22]** Re: [PATCH 2/2] KVM: arm64: Map hyp text as RO and dump instr on
 panic
   - 发件人: Mostafa Saleh <smostafa@google.com>
8. **[07-18 11:35]** Re: [PATCH 2/2] KVM: arm64: Map hyp text as RO and dump instr on
 panic
   - 发件人: Ben Horgan <ben.horgan@arm.com>

---

### Thread 12: [PATCH v4 0/7] Add support for FEAT_{LS64, LS64_V} and related tests

**📧 邮件数**: 8 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 15 Jul 2025 16:13:49 +0800

#### 🤖 AI 总结

本邮件线程讨论了针对 ARMv8.7 架构新增的 FEAT_{LS64, LS64_V} 特性的支持及相关测试。这些特性引入了单拷贝原子 64 字节加载和存储指令，旨在提升用户空间驱动的性能。

**原始 patch/问题内容**：
Yicong Yang 提出的补丁（PATCH v4 0/7）主要目的是为 ARMv8.7 架构的 FEAT_{LS64, LS64_V} 特性添加支持，包括在 CPU 特性列表中标识和启用这些特性、通过 HWCAP3 和 cpuinfo 向用户空间暴露支持情况、添加相关的硬件能力测试，并在虚拟机中处理不支持的内存访问异常。

**之前讨论要点**：
在之前的讨论中，参与者们关注如何在虚拟机中处理 LS64 指令的异常，以及如何确保用户空间能够正确处理这些指令的语义。Marc Zyngier 提出了将用户空间作为处理器异常的接收者，并提供了相应的文档说明。

**本周的新讨论、进展或结论**：
本周的讨论中，Yicong Yang 提交了多个补丁，具体包括：
1. **KVM 支持**：为虚拟机启用 FEAT_{LS64, LS64_V} 特性，确保在合适的条件下用户空间可以使用这些指令。
2. **文档更新**：增加了关于 KVM_EXIT_ARM_LDST64B 的文档，明确用户空间在处理这些指令时的预期行为。
3. **测试用例**：添加了针对 FEAT_{LS64, LS64_V} 的自测案例，确保在支持这些特性的系统上，相关指令能够正常执行而不产生 SIGILL 异常。

整体来看，本周的进展为 ARM 架构的虚拟化支持提供了更为全面的基础，确保了新特性在用户空间和虚拟机中的有效利用。

#### 📝 邮件列表

1. **[07-15 16:13]** [PATCH v4 0/7] Add support for FEAT_{LS64, LS64_V} and related tests
   - 发件人: Yicong Yang <yangyicong@huawei.com>
2. **[07-15 16:13]** [PATCH v4 1/7] KVM: arm64: Add exit to userspace on {LD,ST}64B* outside of memslots
   - 发件人: Yicong Yang <yangyicong@huawei.com>
3. **[07-15 16:13]** [PATCH v4 2/7] KVM: arm64: Add documentation for KVM_EXIT_ARM_LDST64B
   - 发件人: Yicong Yang <yangyicong@huawei.com>
4. **[07-15 16:13]** [PATCH v4 3/7] KVM: arm64: Handle DABT caused by LS64* instructions on unsupported memory
   - 发件人: Yicong Yang <yangyicong@huawei.com>
5. **[07-15 16:13]** [PATCH v4 4/7] arm64: Provide basic EL2 setup for FEAT_{LS64, LS64_V} usage at EL0/1
   - 发件人: Yicong Yang <yangyicong@huawei.com>
6. **[07-15 16:13]** [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Yicong Yang <yangyicong@huawei.com>
7. **[07-15 16:13]** [PATCH v4 6/7] KVM: arm64: Enable FEAT_{LS64, LS64_V} in the supported guest
   - 发件人: Yicong Yang <yangyicong@huawei.com>
8. **[07-15 16:13]** [PATCH v4 7/7] kselftest/arm64: Add HWCAP test for FEAT_{LS64, LS64_V}
   - 发件人: Yicong Yang <yangyicong@huawei.com>

---

### Thread 13: [PATCH 0/5] KVM: arm64: Config driven dependencies for TCR2/SCTLR/MDCR

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 14 Jul 2025 12:54:58 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的配置驱动依赖性，主要涉及 TCR2、SCTLR 和 MDCR 寄存器的转换。

**原始 patch/问题内容**：
Marc Zyngier 提出了一个包含五个补丁的系列，旨在将 TCR2、SCTLR 和 MDCR 寄存器的处理转换为基于配置的清理框架。这是之前在 6.16 版本中未完成的工作。

**之前讨论要点**：
在历史讨论中，Marc 提到这些补丁主要是为了简化寄存器的管理，通过配置驱动的方式来处理寄存器的默认值和特性，确保系统在不同配置下的兼容性和稳定性。

**本周的新讨论、进展或结论**：
在本周的讨论中，Marc 提交了五个补丁，分别针对 TCR2、SCTLR 和 MDCR 寄存器进行了转换，并收紧了 FEAT_PMUv3p9 的定义。Oliver Upton 在最后一封邮件中确认已将这些补丁应用到下一个版本中，表示感谢。这标志着该系列补丁的成功整合，进一步推动了 KVM 在 arm64 架构下的功能完善。

#### 📝 邮件列表

1. **[07-14 12:54]** [PATCH 0/5] KVM: arm64: Config driven dependencies for TCR2/SCTLR/MDCR
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-14 12:54]** [PATCH 1/5] arm64: sysreg: Add THE/ASID2 controls to TCR2_ELx
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[07-14 12:55]** [PATCH 2/5] KVM: arm64: Convert TCR2_EL2 to config-driven sanitisation
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[07-14 12:55]** [PATCH 3/5] KVM: arm64: Convert SCTLR_EL1 to config-driven sanitisation
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[07-14 12:55]** [PATCH 4/5] KVM: arm64: Convert MDCR_EL2 to config-driven sanitisation
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[07-14 12:55]** [PATCH 5/5] KVM: arm64: Tighten the definition of FEAT_PMUv3p9
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[07-16 09:47]** Re: [PATCH 0/5] KVM: arm64: Config driven dependencies for TCR2/SCTLR/MDCR
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 14: [PATCH v3 00/27] KVM: arm64: SCTLR2, DoubleFault2, and NV external abort fixes

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Tue,  8 Jul 2025 10:25:05 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（内核虚拟机）在 arm64 架构下的多个补丁，主要集中在 SCTLR2、DoubleFault2 和 NV 外部中止的修复。

**原始补丁内容**：
Oliver Upton 提出的补丁系列（PATCH v3 00/27）旨在修复与 SCTLR2、DoubleFault2 和 NV 外部中止相关的问题，特别是处理异常的上下文设置和中止的路由行为。

**之前讨论要点**：
在历史讨论中，补丁 v3 版本对 v2 进行了多项改进，包括修正了在 SCLTR2_ELx.NMEA 设置时的掩码计算，统一了对所有中止的 TMEA 处理，并确保在注入中止时正确设置故障上下文。讨论中提到的关键问题是如何处理外部中止的行为，尤其是在不同的虚拟化环境中。

**本周的新讨论与进展**：
本周，Mark Brown 报告了在多个 VHE 平台上运行的外部中止自测失败，追踪后发现问题与最近的补丁有关。Marc Zyngier 进一步分析了异常处理代码的脆弱性，并提出了潜在的修复方案。他指出，当前的实现可能导致 L1 虚拟机错误地处理 SError 中断，并已针对这一问题提交了修复。经过测试，修复后的补丁在 VHE 和 nVHE 环境下均能正确运行外部中止测试，显示出进展。

#### 📝 邮件列表

1. **[07-08 10:25]** [PATCH v3 00/27] KVM: arm64: SCTLR2, DoubleFault2, and NV external abort fixes
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-08 10:25]** [PATCH v3 18/27] KVM: arm64: nv: Take "masked" aborts to EL2 when HCRX_EL2.TMEA is set
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[07-18 23:01]** Re: [PATCH v3 18/27] KVM: arm64: nv: Take "masked" aborts to EL2
 when HCRX_EL2.TMEA is set
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[07-20 11:36]** Re: [PATCH v3 18/27] KVM: arm64: nv: Take "masked" aborts to EL2 when HCRX_EL2.TMEA is set
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[07-20 12:45]** Re: [PATCH v3 18/27] KVM: arm64: nv: Take "masked" aborts to EL2 when HCRX_EL2.TMEA is set
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 15: [PATCH 0/4] KVM: arm64: Userspace GICv3 sysreg access fixes and testing

**📧 邮件数**: 5 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 18 Jul 2025 12:11:50 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（内核虚拟机）在 arm64 架构下的 GICv3 系统寄存器访问问题的修复和测试。Marc Zyngier 提出了四个补丁，旨在解决用户空间无法访问 ICH_HCR_EL2 寄存器的问题。

历史讨论中，Marc 提到之前的补丁存在一个 bug，导致 ICH_HCR_EL2 的位置错误，无法从用户空间访问。补丁的主要内容包括修复寄存器表的排序、确保表格的正确性检查，以及增强自测试以验证寄存器的可访问性。

在本周的新讨论中，Marc 提出了四个具体的补丁：
1. 修复 ICH_HCR_EL2 的排序问题。
2. 清理 sysreg 表检查函数中的参数，确保重置回调的正确性。
3. 强制 GICv3 系统寄存器表的排序，以避免未来的错误。
4. 增加一个自测试，检查 GICv3 系统寄存器的可用性。

这些补丁旨在提高 KVM 的稳定性和可靠性，确保用户空间能够正确访问 GICv3 系统寄存器。

#### 📝 邮件列表

1. **[07-18 12:11]** [PATCH 0/4] KVM: arm64: Userspace GICv3 sysreg access fixes and testing
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-18 12:11]** [PATCH 1/4] KVM: arm64: vgic-v3: Fix ordering of ICH_HCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[07-18 12:11]** [PATCH 2/4] KVM: arm64: Clarify the check for reset callback in check_sysreg_table()
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[07-18 12:11]** [PATCH 3/4] KVM: arm64: Enforce the sorting of the GICv3 system register table
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[07-18 12:11]** [PATCH 4/4] KVM: arm64: selftest: vgic-v3: Add basic GICv3 sysreg userspace access test
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 16: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 11 Jul 2025 12:39:50 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理 SEA（Synchronous External Abort）的问题，主要围绕一个补丁（patch）进行。该补丁的目的是实现虚拟机退出到用户空间，以便处理 SEA。

在历史讨论中，参与者主要集中在补丁的细节上，Oliver Upton 和 Jiaqi Yan 讨论了如何避免在头文件中添加仅在单个调用上下文中使用的辅助函数，以及关于 FEAT_RAS（Reliability, Availability, and Serviceability）特性的细节，强调了在处理阶段-1 和阶段-2 的描述符物理地址时的复杂性。

本周的新讨论中，Jiaqi Yan 表达了对补丁的感谢，并询问是否应该等待 Oliver 发送补丁以便将其合并到 kvmarm/next 分支，或者将其包含在自己的 v3 补丁系列中，并以 Oliver 的名义提交。同时，Jiaqi 提出了将当前补丁集拆分为两个部分的建议：一个专注于 KVM_EXIT_ARM_SEA，另一个用于注入用户补充的异常状态寄存器（esr）。这种拆分可能会加速更重要特性的审查和接受。

#### 📝 邮件列表

1. **[07-11 12:39]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-11 16:59]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
3. **[07-12 12:57]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[07-19 14:24]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>

---

### Thread 17: [PATCH] KVM: arm64: Clear pending exception state before injecting a new one

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 14 Jul 2025 15:46:36 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理异常状态的补丁。原始补丁的目的是在注入新的异常之前，清除任何先前的待处理异常状态，以避免在用户空间重复注入异常时引发警告。

在之前的讨论中，Marc Zyngier 提出了该补丁，指出在用户空间中注入异常时，KVM 可能会丢失已待处理的异常，因此需要在注入新异常之前清除旧的异常状态。补丁的实现通过在 `__kvm_arm_vcpu_set_events` 函数中添加一行代码来清除异常标志。

本周的新讨论中，Oliver Upton 进一步分析了问题，指出补丁可能无法完全解决所有潜在问题，尤其是在处理多个异常时可能仍会触发警告。他提出了一个新的补丁，建议在 `KVM_SET_VCPU_EVENTS` 中立即提交待处理的异常状态，以确保它们在用户空间中被正确处理。Marc Zyngier 对此表示认可，并认为这个方案是合理的。

总结来说，本周的讨论围绕如何更有效地管理 KVM 中的异常状态展开，提出了新的补丁以解决现有问题，并得到了参与者的积极反馈。

#### 📝 邮件列表

1. **[07-14 15:46]** [PATCH] KVM: arm64: Clear pending exception state before injecting a new one
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-14 23:51]** Re: [PATCH] KVM: arm64: Clear pending exception state before
 injecting a new one
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[07-15 09:31]** Re: [PATCH] KVM: arm64: Clear pending exception state before injecting a new one
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 18: [PATCH] KVM: arm64: preserve pending during kvm_irqfd_deassign

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Wed,  2 Jul 2025 07:41:37 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主题为“在 kvm_irqfd_deassign 过程中保留待处理的中断”。该补丁的目的是在调用 `kvm_irqfd_deassign` 时，如果存在待处理的中断，则将其转移到生产者的 eventfd，以便在 KVM 实例被销毁后仍能保留中断状态，便于后续重新创建 KVM 实例时进行中断注入。

在历史讨论中，Steve Sistare 提出了该补丁的初衷，并描述了其在 QEMU 直播更新中的应用。然而，Oliver Upton 指出该方法存在问题，认为在 ITS 映射更新时可能会导致中断丢失或产生错误。Oliver 提到 KVM 已经提供了 `SAVE_PENDING_TABLES` ioctl，用于保存 LPIs 的待处理状态，并建议在用户空间中先完成中断的静默处理。

在本周的新讨论中，Steve Sistare 对 Oliver 的建议表示感谢，并确认他已将 `SAVE_PENDING_TABLES` 添加到 QEMU 直播更新的序列中，成功解决了问题。这表明补丁的实现得到了改进，能够有效地处理待处理中断的状态。

#### 📝 邮件列表

1. **[07-02 07:41]** [PATCH] KVM: arm64: preserve pending during kvm_irqfd_deassign
   - 发件人: Steve Sistare <steven.sistare@oracle.com>
2. **[07-02 08:19]** Re: [PATCH] KVM: arm64: preserve pending during kvm_irqfd_deassign
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[07-14 12:51]** Re: [PATCH] KVM: arm64: preserve pending during kvm_irqfd_deassign
   - 发件人: Steven Sistare <steven.sistare@oracle.com>

---

### Thread 19: [PATCH] KVM: arm64: Filter out HCR_EL2.VSE when running in hypervisor context

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Sun, 20 Jul 2025 12:33:34 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，主要涉及 HCR_EL2.VSE 的处理。原始补丁旨在解决在超管上下文中运行时，HCR_EL2.VSE 可能导致虚拟 SError 被错误地传递给 L1 超管的问题。具体来说，当 L1 超管将 HCR_EL2.VSE 设置为 1 时，可能会在返回 L2 之前触发物理 SError，从而影响系统的稳定性。

在之前的讨论中，Marc Zyngier 提到 HCR_EL2.VSE 仅对 L2 有效，而不应影响 L1，因此需要在进入 L1 主机上下文时过滤掉该位。补丁通过在计算 HCR 时将 HCR_VSE 位清除来实现这一点。

在本周的新讨论中，Marc Zyngier 进一步提出，除了 HCR_EL2.VSE，实际上还应该清除所有不影响 HYP（Hypervisor）上下文的位，并表示他将重新提交一个更完善的补丁，处理与 RAS（Reliability, Availability, and Serviceability）相关的其他问题。整体来看，本周的讨论集中在补丁的改进方向上，强调了对 HYP 上下文的更全面的处理。

#### 📝 邮件列表

1. **[07-20 12:33]** [PATCH] KVM: arm64: Filter out HCR_EL2.VSE when running in hypervisor context
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-20 18:39]** Re: [PATCH] KVM: arm64: Filter out HCR_EL2.VSE when running in
 hypervisor context
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 20: [PATCH v4 05/20] KVM: arm64: timers: Allow physical offset
 without CNTPOFF_EL2

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 9 Jul 2025 16:12:18 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下的定时器问题，特别是允许在没有 CNTPOFF_EL2 的情况下使用物理偏移的补丁（PATCH v4 05/20）。

在历史讨论中，Zenghui Yu 提到在测试 arch_timer_edge_cases 时，发现 test_timer_cval() 在测试物理定时器时返回时间过长。Marc Zyngier 进一步分析了问题，指出内核中的算术运算是基于 64 位值进行的，但实际有效位数不明确，导致计算出不合理的值。由于定时器是以某种方式被仿真，最终可能导致错误的行为。

在本周的新讨论中，Marc Zyngier 继续探讨了这个问题，认为“设置计数器值以计算偏移”的方法在极限情况下并不实用。他提到 VM_COUNTER_OFFSET 方法更为一致，能够避免上述计算问题。同时，他表达了希望 QEMU 能够采用这种方法，并建议增加相关测试。

总体来看，讨论集中在如何有效处理定时器偏移的问题，以及对现有方法的改进建议。

#### 📝 邮件列表

1. **[07-09 16:12]** Re: [PATCH v4 05/20] KVM: arm64: timers: Allow physical offset
 without CNTPOFF_EL2
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>
2. **[07-19 13:04]** Re: [PATCH v4 05/20] KVM: arm64: timers: Allow physical offset without CNTPOFF_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 21: [PATCH] KVM: arm64: Check for SYSREGS_ON_CPU before accessing the CPU state

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sun, 20 Jul 2025 11:22:29 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，主要内容是检查 SYSREGS_ON_CPU 标志，以确保在访问 CPU 状态之前进行必要的验证。

**原始补丁内容**：
补丁由 Marc Zyngier 提出，目的是在访问 CPU 状态之前检查 SYSREGS_ON_CPU 标志，以解决 Mark Brown 报告的一个问题：在不加载 vcpu 的情况下使异常可见的代码在 VHE（Virtualization Host Extensions）上存在缺陷，导致外部中止自测失败。

**之前讨论要点**：
在历史讨论中，虽然没有具体的邮件记录，但可以推测该问题的背景涉及到 KVM 在处理异常时的系统寄存器可见性，尤其是在 VHE 环境下的实现细节。

**本周的新讨论与进展**：
本周的讨论集中在补丁的具体实现上，Marc Zyngier 在补丁中添加了必要的检查，并且在代码中明确记录了在调用相关辅助函数（__vcpu_write_sys_reg_to_cpu 和 __vcpu_read_sys_reg_from_cpu）之前必须检查 SYSREGS_ON_CPU 标志。补丁的修改涉及到两个文件，增加了必要的条件判断，以确保系统寄存器的正确访问，防止潜在的错误发生。

#### 📝 邮件列表

1. **[07-20 11:22]** [PATCH] KVM: arm64: Check for SYSREGS_ON_CPU before accessing the CPU state
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 GIT PULL

共 2 个 thread

---

### Thread 1: [GIT PULL] irqchip: Add GICv5 support

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 17 Jul 2025 13:23:06 +0100

#### 🤖 AI 总结

本邮件讨论的主题是为 Linux 内核添加 GICv5 支持的补丁。Marc Zyngier 提出了这个补丁请求，主要目的是为新的 arm64 GICv5 架构提供主机内核支持，包括中断路由、交付到 CPU、固定中断、MSI 和中断转换等功能。补丁经过了一段时间的测试，只有一个回归问题被报告并迅速修复。

在之前的讨论中，Marc 提到仍有一些补丁在审查中，主要针对错误处理路径，但他认为没有必要再拖延这个补丁的合并，可以在后续版本中添加这些修复。此外，GICv5 的支持对于在 GICv5 主机上启用 GICv3 兼容性至关重要。

在本周的新讨论中，Thomas Gleixner 表示支持将该补丁保留在 kvmarm 树中，前提是它将在下一个合并窗口中使用。如果 kvmarm 的内容尚未准备好，他愿意将其合并。Marc 随后确认 kvmarm 的相关内容也已准备就绪，并计划在 6.17 版本中发布。

总结而言，GICv5 支持的补丁已准备好合并，相关讨论表明各方对其进展持积极态度。

#### 📝 邮件列表

1. **[07-17 13:23]** [GIT PULL] irqchip: Add GICv5 support
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-18 23:26]** Re: [GIT PULL] irqchip: Add GICv5 support
   - 发件人: Thomas Gleixner <tglx@linutronix.de>
3. **[07-19 08:32]** Re: [GIT PULL] irqchip: Add GICv5 support
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [GIT PULL] KVM/arm64 fixes for 6.16, take #6

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 11 Jul 2025 09:48:34 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM/arm64 的修复补丁，旨在解决 6.16 版本中的一个问题。历史讨论中，Marc Zyngier 提出了一个补丁，主要针对嵌套虚拟化中 PMU 寄存器数量的清理问题，称其为“脑筋急转弯”。他请求 Paolo 进行合并，并提供了相关的 Git 仓库链接。

在本周的新讨论中，Paolo Bonzini 确认已经将该补丁合并，表示感谢。这表明该补丁得到了认可，并成功纳入了主线代码。

总结来看，历史讨论中提出的补丁针对嵌套虚拟化的 PMU 寄存器问题，经过讨论后在本周得到了合并，标志着该问题的解决。

#### 📝 邮件列表

1. **[07-11 09:48]** [GIT PULL] KVM/arm64 fixes for 6.16, take #6
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-17 17:10]** Re: [GIT PULL] KVM/arm64 fixes for 6.16, take #6
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

## 📌 Other

共 1 个 thread

---

### Thread 1: [syzbot] [kvmarm?] WARNING in pend_sync_exception

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Sat, 12 Jul 2025 18:45:31 -0700

#### 🤖 AI 总结

本邮件线程讨论了在 KVM ARM 虚拟化环境中出现的一个警告问题，具体是关于 `pend_sync_exception` 的警告。

1. **原始 patch/问题的内容**：历史讨论中，syzbot 报告了在特定的内核提交（15724a984643）中发现的 `pend_sync_exception` 警告。该问题出现在 KVM ARM 虚拟化环境中，影响了系统的稳定性。

2. **之前的讨论要点**：在历史邮件中，syzbot 提供了详细的错误信息和相关的环境配置链接，旨在引起开发者的注意并促使对该问题的修复。

3. **本周的新讨论、进展或结论**：在本周的讨论中，Marc Zyngier 提出了一个新的测试 patch，旨在修复该问题。随后，syzbot 对该 patch 进行了测试，结果显示在新的提交（e62014ac）中，重现问题的测试用例未再触发任何警告，表明该问题已得到解决。测试结果也被记录并确认，显示出该 patch 的有效性。

总体来看，本周的讨论表明，针对 `pend_sync_exception` 的问题已经通过新的修复 patch 得到了有效解决。

#### 📝 邮件列表

1. **[07-12 18:45]** [syzbot] [kvmarm?] WARNING in pend_sync_exception
   - 发件人: syzbot <syzbot+4e09b1432de3774b86ae@syzkaller.appspotmail.com>
2. **[07-14 14:29]** Re: [syzbot] [kvmarm?] WARNING in pend_sync_exception
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[07-14 07:21]** Re: [syzbot] [kvmarm?] WARNING in pend_sync_exception
   - 发件人: syzbot <syzbot+4e09b1432de3774b86ae@syzkaller.appspotmail.com>

---

