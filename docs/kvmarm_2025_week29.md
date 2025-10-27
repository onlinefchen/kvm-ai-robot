# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 11:29:55

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

本邮件讨论的主题是关于KVM（Kernel-based Virtual Machine）中支持非CoCo虚拟机的guest_memfd（来宾内存文件描述符）内存映射的补丁系列。以下是讨论的主要内容：

1. **原始补丁内容**：
   - 提交的补丁系列（[PATCH v14 00/21]）旨在为非CoCo虚拟机启用host用户空间映射guest_memfd支持的内存。这一功能对多个KVM用例至关重要，例如允许Firecracker等虚拟机管理程序完全基于guest_memfd运行来宾。

2. **历史讨论要点**：
   - 之前的讨论集中在如何将guest_memfd与“私有”内存的概念解耦，确保支持非私有内存的映射。补丁中引入了多个新的Kconfig选项和功能，以支持guest_memfd的映射和故障处理。

3. **本周的新讨论与进展**：
   - 本周的讨论主要集中在补丁的具体实现和命名上，包括对Kconfig选项的重命名（如将CONFIG_KVM_PRIVATE_MEM改为CONFIG_KVM_GMEM），以及对函数和变量的命名进行清晰化处理。
   - 参与者对补丁的细节进行了审查，提出了对命名和功能的不同看法，特别是关于如何处理guest_memfd的映射支持。
   - 讨论还涉及到如何在不同VM类型中启用guest_memfd的映射支持，以及如何在自测中确保功能的正确性。

总体而言，此次讨论围绕着如何优化和扩展KVM对guest_memfd的支持，确保其在不同虚拟机类型中的一致性和安全性。

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

本邮件线程讨论了一个关于 KVM 的补丁系列，主要目标是为非 CoCo 虚拟机启用主机用户空间映射的 guest_memfd 支持。该补丁系列包含 21 个补丁，主要修改了 KVM 的内存管理和映射机制。

**补丁内容**：
补丁的核心是允许主机用户空间通过 mmap() 映射 guest_memfd 支持的内存。这一功能对于多个 KVM 用例至关重要，例如支持 Firecracker 运行完全由 guest_memfd 支持的虚拟机，增强安全性，消除直接映射的需求等。

**历史讨论要点**：
在之前的讨论中，参与者们关注了如何将 guest_memfd 的支持扩展到非私有内存，并对相关的 Kconfig 选项进行重命名，以更准确地反映其功能。同时，补丁中还引入了新的能力标志 KVM_CAP_GMEM_MMAP，以便用户空间能够检测到该功能的支持。

**本周新讨论与进展**：
本周的讨论集中在补丁的具体实现和代码审查上。参与者对补丁的各个方面进行了审查，并提出了改进建议，例如在处理内存故障时增加对 guest_memfd 的支持。Xiaoyao Li 提出了对某些补丁的具体反馈，强调了代码的清晰性和功能的准确性。此外，补丁的实现已获得多个参与者的认可，计划在 QEMU 中进行进一步的测试，以验证非 CoCo 虚拟机的功能。

总体而言，这一系列补丁的实施将显著增强 KVM 的内存管理能力，特别是在支持 guest_memfd 方面，为未来的虚拟化用例奠定了基础。

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

本邮件线程讨论的主题是关于 ARM64 PMU（性能监控单元）分区的补丁系列（[PATCH v4 00/23]）。该补丁旨在为 ARM 架构引入一种新的 PMU 分区方案，允许为虚拟机（guest）保留一部分计数器，从而显著降低性能开销。

**原始补丁/问题内容**：
补丁系列的核心是实现 PMU 的分区，使得虚拟机可以直接访问某些计数器，减少对宿主机的干扰。补丁中包含多个功能的实现，如懒惰上下文切换、对 PMU 控制的改进等。

**之前讨论要点**：
在历史讨论中，参与者讨论了 PMU 分区的必要性及其对性能的影响，强调了在虚拟化环境中减少开销的重要性。补丁的设计考虑了如何安全地管理 PMU 访问，并确保在分区模式下的稳定性和安全性。

**本周的新讨论、进展或结论**：
本周的讨论集中在补丁的具体实现上，包括如何处理 PMU 中的不同寄存器、如何在上下文切换时管理寄存器状态，以及如何在分区模式下处理中断。Colton Lewis 提出了多个补丁，逐步完善了 PMU 的分区功能，并增加了对分区 PMU 的支持的测试用例。此外，邮件中提到了一些编译错误和警告，开发者计划修复这些问题以确保补丁的稳定性和兼容性。

总结来说，此次讨论围绕 ARM64 PMU 的分区功能展开，旨在通过改进虚拟机对 PMU 的访问方式来提升性能，同时确保系统的安全性和稳定性。

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

在本次邮件讨论中，主题为「[PATCH v3 08/10] KVM: arm64: Handle FFA_MEM_LEND calls from the host」，主要涉及 KVM 在 arm64 架构下如何处理来自主机的 FFA_MEM_LEND 调用。

**原始 patch/问题的内容**：
该补丁旨在实现 KVM 对 FFA_MEM_LEND 调用的支持，以便在主机与虚拟机之间进行内存借用。

**之前讨论要点**：
在历史讨论中，Will Deacon 指出 pKVM 并不使用 FF-A 来管理主机与客机之间的页面所有权，FF-A 仅用于安全世界的内存管理。LEND 事务意味着安全世界必须防止非安全访问，而不应依赖 pKVM 进行解除映射。

**本周的新讨论、进展或结论**：
本周的讨论中，DaeRo Lee 提出了对 pKVM 策略的质疑，询问是否 pKVM 不管理非安全内存，而 FF-A 规范支持在非安全虚拟机之间进行内存管理。他进一步探讨了如何通过 FF-A 从主机向客机借用内存，以及 pKVM 是否能够阻止这种操作。Will Deacon 建议查看代码以获取更多信息，显示出对该问题的关注，但并未给出明确的解决方案。整体来看，本周的讨论主要集中在对 pKVM 策略的理解和潜在的实现细节上。

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

本邮件线程讨论了一个关于 Linux 内核的补丁系列，主题为“stackleak: 支持 Clang 栈深度跟踪”。该补丁系列的主要目的是将现有的 GCC 插件替换为 Clang 的实现，以增强内核的安全性。

**原始补丁内容**：
补丁系列的核心是实现 Clang 的栈深度跟踪功能，具体包括将原有的 `STACKLEAK` 功能重命名为 `KSTACK_ERASE`，并为其添加新的配置选项。这一功能的实现依赖于 Clang 的栈深度跟踪回调。

**之前讨论要点**：
在历史讨论中，参与者们讨论了如何将现有的 GCC 插件与 Clang 的实现相结合，确保在不同架构上都能有效工作。补丁的设计考虑了多种架构的特性，并进行了相应的代码调整。

**本周新讨论和进展**：
本周的讨论集中在补丁的具体实现上，Kees Cook 提出了多个补丁，解决了不同架构（如 x86、ARM、MIPS 和 s390）中与 KCOV 相关的 `__init` 和内联函数的不匹配问题。此外，补丁还包括对 Clang 21 新增的栈深度跟踪回调的支持。参与者们对补丁进行了审查和反馈，确认了补丁的有效性和必要性。

整体来看，本周的讨论推动了补丁的进一步完善，确保了内核在安全性和性能方面的提升。

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

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的用户空间寄存器可见性修复的补丁系列（共11个补丁）。这些补丁旨在解决 EL2 GICv3 寄存器暴露不一致的问题，并改进寄存器的可见性和文档。

历史讨论中，Marc Zyngier 提到当前通过 ONE_REG 接口暴露的 EL2 GICv3 寄存器与 KVM_DEV_ARM_VGIC_GRP_CPU_SYSREGS 接口不一致，导致用户空间无法正确访问这些寄存器。补丁包括修复 RVBAR_EL2 的访问、隐藏不应暴露的寄存器、根据功能可用性条件性暴露 FEAT_FGT 寄存器等。

在本周的新讨论中，Marc Zyngier 提交了多个补丁，逐一修复了上述问题，并进行了自测，所有测试均通过。补丁包括：
1. 将 RVBAR_EL2 的访问设为 UNDEF。
2. 隐藏 ICH_*_EL2 寄存器的暴露。
3. 定义 ICC_SRE_EL2 的常量值。
4. 使 GICv3 的保存/恢复遵循可见性属性。
5. 通过 KVM_DEV_ARM_VGIC_GRP_CPU_SYSREGS 接口暴露 GICv3 EL2 寄存器。
6. 条件性暴露 FGT 和 FGT2 寄存器。
7. 更新自测代码以简化寄存器与功能的依赖关系，并添加 EL2 寄存器的测试。

最后，Marc Zyngier 表示这些补丁已应用到下一个开发分支，并感谢参与者的贡献。

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

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上对 GICD_TYPER2.nASSGIcap 寄存器的写入支持的补丁系列。该补丁旨在允许用户空间在初始化 VGIC（Virtual Generic Interrupt Controller）之前修改 GICD_TYPER2.nASSGIcap 的值，以便更好地控制虚拟处理器（vPE）分配。

在历史讨论中，Oliver Upton 提出了多个补丁，包括对 VGICv3 相关寄存器的访问控制、对 vSGIs（虚拟共享中断）和 vLPIs（虚拟本地中断）的支持等。特别是补丁 v4 4/6 允许用户空间在 VGIC 初始化前写入 GICD_TYPER2.nASSGIcap，以便在资源受限的环境中进行更灵活的 vPE 分配。

在本周的新讨论中，Eric Auger 对多个补丁进行了审查，提出了一些建议和问题，主要集中在补丁的描述和代码逻辑的清晰性上。他对补丁 v4 1/6、v4 2/6、v4 4/6、v4 5/6 和 v4 6/6 表示支持，并提供了具体的改进建议，强调了需要更清晰的文档说明和代码逻辑的合理性。

总体而言，本周的讨论主要是对补丁的审查和建议，未提出新的反对意见，显示出对补丁系列的认可。

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

本邮件线程讨论了针对 KVM（内核虚拟机）在 arm64 架构上支持 FF-A 1.2 及 SEND_DIRECT2 ABI 的补丁集（PATCH v7 0/5）。FF-A 1.2 规范引入了新的 SEND_DIRECT2 ABI，允许使用 x4-x17 寄存器作为消息负载。补丁集的主要目的是防止主机使用低于已与虚拟机监控器协商的 FF-A 版本，从而确保兼容性。

在历史讨论中，参与者主要关注补丁的实现细节，特别是 SMCCC 1.2 的使用和寄存器的处理。Marc Zyngier 对某些寄存器的处理提出了质疑，认为在不符合规范的情况下进行更改可能导致问题。Per Larsen 则解释了使用零填充未使用寄存器的合规性。

在本周的新讨论中，Will Deacon 对补丁提出了进一步的建议，认为应将某些补丁拆分为更小的单元，以便于管理和理解。他指出，检查某些位的必要性值得商榷，并建议在后续版本中解决 Marc 的反馈。此外，Per Larsen 表示将根据反馈调整补丁集，确保更好地满足规范要求。

总的来说，本周的讨论集中在补丁的细节优化和规范遵循上，推动了补丁集的进一步完善。

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

本邮件讨论的主题是关于一个补丁系列（PATCH v13 00/20），旨在为非CoCo虚拟机（VM）启用主机用户空间对基于guest_memfd的内存的映射。该补丁的主要变更包括重命名函数和变量、扩展提交信息，并基于Linux 6.16-rc5进行重整。此补丁的实施将支持如Firecracker等虚拟机管理程序（VMM）完全使用guest_memfd作为内存后端，从而简化内存管理模型。

在历史讨论中，参与者们主要关注补丁在处理基于guest_memfd的内存页故障时的逻辑，特别是如何避免与内存无效化（如fallocate(PUNCH_HOLE)）的竞争条件。Marc Zyngier和Roy Patrick提出了对现有逻辑的改进建议，强调需要在故障处理时考虑内存状态的变化。

在本周的新讨论中，Fuad Tabba和Marc Zyngier达成一致，决定在处理逻辑中使用VM_WARN_ON_ONCE()，以替代即将废弃的VM_BUG_ON。这一决定表明参与者们对补丁的进一步细化和优化达成了共识，且没有发现新的问题或争议。整体来看，讨论进展顺利，补丁的实施路径逐渐明朗。

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构上对 FF-A 1.2 及 SEND_DIRECT2 ABI 的支持，涉及一系列补丁（patch）更新。

1. **原始 patch/问题的内容**：该补丁集的主要目的是实现 FF-A 1.2 规范中的 SEND_DIRECT2 ABI，允许使用寄存器 x4-x17 作为消息负载。补丁确保主机不会使用低于与虚拟机管理程序（hypervisor）协商的 FF-A 版本，因为低版本不具备必要的兼容性路径。

2. **之前讨论要点**：在历史讨论中，补丁的多个版本经历了多次修改，主要集中在对 SMCCC 1.2 的支持、更新接口的可选性以及对不支持接口的标记等方面。补丁的更新旨在简化实现并确保与 FF-A 1.2 的兼容性。

3. **本周的新讨论、进展或结论**：本周的讨论中，Per Larsen 提交了七个补丁，主要包括：
   - 修正主机版本降级尝试的返回值。
   - 更新 FF-A 初始化和主机处理程序以使用 SMCCC 1.2。
   - 将 FFA_NOTIFICATION_* 接口标记为不支持，防止其传递到安全区（TZ）。
   - 更新对 FF-A 1.2 接口的支持，标记不支持的接口，并掩码 FFA_FEATURE 调用的响应。
   - 将支持的 FF-A 版本提升至 1.2，并在主机处理程序中添加对 FFA_MSG_SEND_DIRECT_REQ2 的支持。

整体而言，本周的讨论和补丁更新进一步推动了对 FF-A 1.2 的支持，确保了与新规范的兼容性，同时也处理了不支持接口的相关问题。

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
本次补丁系列包含两个主要部分：第一个补丁为 nvhe 添加了在崩溃时转储故障指令的支持；第二个补丁则为 pKVM 添加类似的支持，并将 hypervisor 代码映射为只读（RO），以便在崩溃时进行信息提取。

**之前讨论要点**：
在历史讨论中，补丁的设计思路得到了阐述，特别是如何在崩溃时读取和转储指令。最初的设计是基于 nvhe 的调试配置（CONFIG_NVHE_EL2_DEBUG），但在后续讨论中，参与者提出了将此功能扩展到 pKVM 的必要性。

**本周新讨论及进展**：
本周的讨论主要集中在补丁的细节和合并策略上。Mostafa Saleh 提出了将两个补丁分开处理的理由，以便于更容易地进行合并。Ben Horgan 对此表示理解，并讨论了补丁顺序的调整。最终，大家达成共识，认为分开补丁的做法是合理的，并没有强烈的反对意见。

总体来看，本周的讨论推动了补丁的进一步完善，确保在内核崩溃时能够有效地转储故障信息，从而提高调试效率。

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

本邮件线程讨论了对 Armv8.7 架构中新引入的 64 字节原子加载和存储指令（FEAT_{LS64, LS64_V}）的支持，主要由 Yicong Yang 提出并进行补丁开发。

**原始 patch/问题内容**：
该补丁的目标是添加对 FEAT_{LS64, LS64_V} 的支持，包括在 CPU 特性列表中识别和启用这些功能，向用户空间暴露相关信息，并处理虚拟机中对不支持内存访问的异常。

**之前讨论要点**：
在历史讨论中，补丁经历了多次修改，主要集中在如何处理虚拟机中对不支持内存的访问，以及如何将相关功能暴露给用户空间。Marc Zyngier 提供了处理 LS64 异常的补丁，并强调了用户空间需要处理这些指令的语义。

**本周的新讨论、进展或结论**：
本周的讨论主要围绕补丁的具体实现细节，包括：
1. **补丁实现**：Yicong Yang 提交了多个补丁，涵盖了对 FEAT_{LS64, LS64_V} 的支持、KVM 的相关文档更新、以及对用户空间的测试等。
2. **测试情况**：补丁经过测试，确认在支持这些特性的系统上，相关指令可以正常执行而不会引发 SIGILL 错误。
3. **文档更新**：增加了对 KVM_EXIT_ARM_LDST64B 的文档说明，明确用户空间在处理这些指令时的预期行为。

整体来看，本周的讨论和补丁提交为 Armv8.7 架构的 64 字节原子操作提供了更为全面的支持，确保了虚拟化环境中的兼容性和功能性。

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的配置驱动依赖性，主要涉及 TCR2、SCTLR 和 MDCR 寄存器的改动。

1. **原始 patch/问题的内容**：
   本次讨论包含五个补丁，旨在将 TCR2、SCTLR 和 MDCR 寄存器的某些功能转换为配置驱动的消毒框架。这些补丁是之前 6.16 版本系列的延续，主要是为了清理和优化代码。

2. **之前的讨论要点**：
   在历史讨论中，Marc Zyngier 提到这些补丁是为了进一步完善 KVM 的寄存器管理，确保寄存器的行为能够根据配置进行调整，以提高系统的灵活性和安全性。

3. **本周的新讨论、进展或结论**：
   本周的讨论中，Marc Zyngier 提交了五个补丁，分别是：
   - 添加 TCR2_ELx 的 THE/ASID2 控制。
   - 将 TCR2_EL2 转换为配置驱动的消毒。
   - 将 SCTLR_EL1 转换为配置驱动的消毒。
   - 将 MDCR_EL2 转换为配置驱动的消毒。
   - 收紧 FEAT_PMUv3p9 的定义。
   最后，Oliver Upton 确认已将这些补丁应用到下一个版本中，表明这些更改得到了认可并将继续推进。

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

本邮件线程讨论了针对 KVM（内核虚拟机）在 arm64 架构上的一系列补丁，主要集中在 SCTLR2、DoubleFault2 和 NV 外部中止的修复。

**原始补丁内容**：
补丁 v3 主要修复了与 SCTLR2_ELx.NMEA 设置相关的掩码计算问题，整合了所有中止的 TMEA 处理，并确保在注入中止时正确设置故障上下文。此外，补丁还解决了在未实现 FEAT_RAS 的情况下不应使用来宾虚拟机的 VSESR 的问题。

**之前讨论要点**：
在历史讨论中，开发者们关注了补丁的有效性和潜在问题，特别是在处理外部中止时的复杂性。补丁的设计旨在提高 KVM 的稳定性和兼容性，但也引发了对其在不同平台上的测试结果的关注。

**本周新讨论与进展**：
本周的讨论中，Mark Brown 报告了在多个平台上运行的外部中止自测失败，指出了补丁可能引入的错误。Marc Zyngier 随后确认了异常处理代码的脆弱性，并提出了修复建议。他发现 L1 来宾可能错误地观察到 SError，而不是 L2 的中止，导致了系统崩溃。Marc 提出了两个修复方案，并表示在他的测试环境中，外部中止测试在 VHE 和 nVHE 来宾中均能正确运行。

整体来看，虽然补丁旨在解决多个问题，但在实施过程中发现了新的问题，开发者们正积极寻求解决方案以确保 KVM 的稳定性。

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下对 GICv3（通用中断控制器版本3）系统寄存器访问的修复和测试。Marc Zyngier 提出了四个补丁（patch），旨在解决用户空间无法访问 ICH_HCR_EL2 寄存器的问题。

历史讨论中，Marc 提到之前的补丁存在问题，导致 ICH_HCR_EL2 的位置错误，影响了系统寄存器表的排序和访问。为此，他提出了补丁以修复寄存器表的顺序，并确保所有寄存器表都经过排序检查。

在本周的新讨论中，Marc 提出了四个具体的补丁：
1. 修复 ICH_HCR_EL2 的排序问题。
2. 明确检查系统寄存器表的重置回调。
3. 强制要求 GICv3 系统寄存器表的排序。
4. 添加基本的 GICv3 系统寄存器用户空间访问测试，以确保这些寄存器的可用性。

这些补丁的实施将有助于提高 KVM 在 arm64 架构下的稳定性和可靠性，确保用户空间能够正确访问 GICv3 系统寄存器。

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理 SEA（Synchronous External Abort）时的 VM 退出到用户空间的补丁（PATCH v2 1/6）。该补丁旨在改进 KVM 对于外部中断的处理，特别是在处理不同阶段的描述符时的行为。

在历史讨论中，参与者 Oliver Upton 和 Jiaqi Yan 针对补丁的细节进行了深入交流。Oliver 提出了避免在头文件中添加仅在单个调用点使用的辅助函数的建议，并讨论了如何在不同的内存访问阶段区分错误来源。Jiaqi 也表示将基于这些反馈进行补丁的更新。

在本周的新讨论中，Jiaqi 表达了对补丁的感谢，并询问是否应该等待 Oliver 提交补丁以便于他进行基于此的 v3 版本更新。Jiaqi 还提出了将当前补丁集拆分为两个部分的建议，以便更快地审核和接受 KVM_EXIT_ARM_SEA 这一更重要的功能，同时计划单独发送一个补丁集来增强客户机的 SEA 注入功能。

总体来看，本周讨论集中在补丁的进一步优化和版本管理上，显示出参与者之间的协作和对改进的积极态度。

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

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 ARM64 架构下处理异常的补丁，主题为“在注入新异常之前清除待处理异常状态”。

**原始补丁内容**：
Marc Zyngier 提出的补丁旨在解决在用户空间重复注入异常时，KVM 可能会丢失已待处理异常的问题。补丁的核心是无条件地在注入新异常之前清除任何先前的异常状态，以避免警告信息的产生。

**之前的讨论要点**：
在本周之前的讨论中，Oliver Upton 提到，现有的 ABI 允许在同一 ioctl 中注入多个异常，这可能导致警告的触发。此外，KVM_GET_VCPU_EVENTS 对待处理的 SEA（Synchronous Exception Acknowledgment）处理不当，实际上这些异常是延迟到下次 KVM_RUN 调用时才会被处理。

**本周的新讨论与进展**：
本周，Oliver Upton 提出了一个新的补丁，旨在立即提交 KVM_SET_VCPU_EVENTS 中的待处理异常，以解决前述问题。他指出，这种处理方式与 KVM_RUN 中对 KVM 注入异常的处理方式一致。Marc Zyngier 对此补丁表示认可，并提出了对 commit helper 使用的建议。整体来看，讨论集中在如何更有效地管理和提交异常状态，以提高 KVM 的稳定性和可靠性。

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

本邮件线程讨论了一个关于 KVM（内核虚拟机）在 ARM64 架构下的补丁，主要涉及在调用 `kvm_irqfd_deassign` 时如何保留待处理的中断状态。

**原始 patch/问题内容**：
Steve Sistare 提出的补丁旨在确保在调用 `kvm_irqfd_deassign` 时，如果中断在 `irq->pending_latch` 中待处理，则将其转移到生产者的 eventfd 中。这样，如果 KVM 实例随后被销毁，中断状态将保留在生产者中，便于在新 KVM 实例中重新创建时进行处理。

**之前讨论要点**：
Oliver Upton 对该补丁提出了质疑，指出在 ITS 映射更新过程中可能会出现非原子性的问题，导致中断丢失或产生错误。此外，他提到 KVM 已经提供了 `SAVE_PENDING_TABLES` ioctl，用于保存 LPIs 的待处理状态，并期望用户空间在调用时已经对中断进行了静默处理。

**本周的新讨论、进展或结论**：
在本周的讨论中，Steve Sistare 感谢 Oliver 的建议，并表示已将 `SAVE_PENDING_TABLES` 添加到 QEMU 的实时更新序列中，紧接在调用 `kvm_irqfd_deassign` 之后，这一调整成功解决了问题。

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

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主题为“在虚拟化上下文中过滤 HCR_EL2.VSE”。该补丁的目的是解决在 L1 超级管理程序（hypervisor）中处理虚拟 SError 时的一个问题。具体来说，当 L1 超级管理程序将 HCR_EL2.VSE 设置为 1 时，可能会错误地将虚拟 SError 视为物理 SError，从而影响系统的稳定性。

在历史讨论中，补丁的背景并未详细展开，但可以推测该问题与之前的补丁（04ab519bb86df）有关，该补丁配置了 HCR_EL2 以支持 FEAT_NV2 特性。

在本周的新讨论中，Marc Zyngier 提出了该补丁的具体实现，指出在计算主机的 HCR_EL2 值时，应该过滤掉 HCR_EL2.VSE，以确保它只适用于 L2，而不影响 L1。Marc 还提到，未来的修复方案可能会更进一步，清除所有不影响 HYP 上下文的位，除了 RES1 位，并表示将在处理完其他 RAS 启用相关事务后重新提交补丁。

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

在本邮件线程中，讨论的主题是一个针对 KVM（内核虚拟机）在 arm64 架构上的定时器补丁，具体内容为“允许在没有 CNTPOFF_EL2 的情况下使用物理偏移”。该补丁旨在解决在测试物理定时器时遇到的性能问题。

在历史讨论中，Zenghui Yu 提到他在 Kunpeng920 上测试 arch_timer_edge_cases 时发现，测试物理定时器的 `test_timer_cval()` 函数返回时间过长，暗示了定时器在某些情况下的表现不理想。Marc Zyngier 进一步指出，内核中的算术运算是基于 64 位值进行的，但实际有效位数不明确，导致计算结果异常，影响定时器的模拟效果。

本周的新讨论中，Marc Zyngier 对之前的问题进行了总结，认为“设置计数器值以计算偏移”的方法在极限情况下并不实用。他提到 VM_COUNTER_OFFSET 方法更为一致，能够避免上述计算错误。同时，他希望 QEMU 能够支持这一方法，并建议添加相关测试，以确保其有效性。

总体来看，讨论围绕如何优化 KVM 的定时器处理，尤其是在物理偏移的计算上，提出了更为合理的解决方案。

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，主要涉及在访问 CPU 状态之前检查 SYSREGS_ON_CPU 标志。

**原始补丁内容**：
Marc Zyngier 提出的补丁旨在修复一个问题，即在异常处理时未检查系统寄存器是否已加载，导致在 VHE（Virtualization Host Extensions）模式下的代码出现错误。补丁要求在调用相关的寄存器读写辅助函数之前，必须检查 SYSREGS_ON_CPU 标志。

**之前讨论要点**：
在历史讨论中，Mark Brown 报告了由于提交使异常可见而不需要加载 vcpu，导致外部中止自测失败的问题。经过调查发现，相关代码在 VHE 模式下完全失效，虽然之前未出现问题，但这种情况显然是不可接受的。

**本周的新讨论与进展**：
本周的讨论集中在补丁的具体实现上，Marc Zyngier 提供了补丁的详细修改，包括在相关代码中添加必要的检查，并在文档中强调了检查 SYSREGS_ON_CPU 标志的重要性。补丁已提交并包含了对两个文件的修改，确保在访问系统寄存器之前进行适当的检查，以避免潜在的错误。

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

本邮件线程讨论了为 Linux 内核添加 GICv5 支持的补丁。该补丁旨在为新的 arm64 GICv5 架构提供主机内核支持，涵盖了中断路由、交付、MSI 和中断翻译等功能。

在历史讨论中，虽然没有详细记录，但可以推测该补丁经过了一段时间的测试，只有一个回归问题被报告并已修复。补丁的提交者 Marc Zyngier 表示，尽管还有一些补丁在审查中，但没有理由再拖延提交。

在本周的新讨论中，Marc Zyngier 提交了 GICv5 核心基础设施的拉取请求，并提到该补丁已在 -next 分支上稳定运行。参与者 Thomas Gleixner 表示支持将该补丁保留在 kvmarm 树中，前提是它将在下一个合并窗口中使用。Marc 随后确认 kvmarm 的相关内容也已准备就绪，并计划在 6.17 版本中发布。

总体来看，本周的讨论主要集中在确认 GICv5 支持的补丁准备情况及其合并计划上，显示出对新架构支持的积极推进。

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

本邮件讨论的主题是关于 KVM/arm64 在 6.16 版本中的修复，Marc Zyngier 提出了一个补丁，旨在解决在嵌套虚拟化中处理 PMU（性能监控单元）寄存器数量时的一个问题。Marc 形容这个问题为“脑筋急转弯”，并希望这次修复能够成为最终版本。

在历史讨论中，Marc 提到自上一个提交以来的一些变更，并提供了相关的 Git 仓库链接，以便 Paolo 进行拉取操作。

在本周的新讨论中，Paolo Bonzini 对 Marc 的补丁表示感谢，并确认已将其拉取。这表明补丁得到了认可，并将被纳入后续的版本中。

总结来说，Marc 提出的补丁解决了嵌套虚拟化中的 PMU 寄存器问题，经过讨论后已被 Paolo 接受并拉取，标志着该问题的修复进程顺利推进。

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

本邮件讨论主题为“[syzbot] [kvmarm?] WARNING in pend_sync_exception”，主要涉及在 KVM ARM64 环境中出现的一个警告问题。

1. **原始 patch/问题的内容**：历史讨论中，syzbot 报告了在特定的内核提交（15724a984643）中，出现了 pend_sync_exception 的警告。该问题与 KVM ARM64 的异常处理相关，可能影响系统的稳定性。

2. **之前的讨论要点**：在历史邮件中，syzbot 提供了详细的错误日志和内核配置链接，供开发者分析和调试。该问题引起了对 KVM ARM64 代码的关注，开发者们开始探讨可能的修复方案。

3. **本周的新讨论、进展或结论**：本周的讨论中，Marc Zyngier 提出了一个新的测试补丁，并请求进行测试。随后，syzbot 对该补丁进行了测试，结果显示该补丁成功解决了之前报告的问题，未再触发任何警告。测试结果表明，补丁在特定的内核提交（e62014ac）上有效，且测试由机器人自动执行，结果为最佳努力。

总体来看，本周的进展表明，针对 pend_sync_exception 问题的补丁已成功应用，问题得到解决。

#### 📝 邮件列表

1. **[07-12 18:45]** [syzbot] [kvmarm?] WARNING in pend_sync_exception
   - 发件人: syzbot <syzbot+4e09b1432de3774b86ae@syzkaller.appspotmail.com>
2. **[07-14 14:29]** Re: [syzbot] [kvmarm?] WARNING in pend_sync_exception
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[07-14 07:21]** Re: [syzbot] [kvmarm?] WARNING in pend_sync_exception
   - 发件人: syzbot <syzbot+4e09b1432de3774b86ae@syzkaller.appspotmail.com>

---

