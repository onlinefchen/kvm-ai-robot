# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 10:17:31

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 306
- **总 Thread 数**: 27
- **大型 Thread** (>20封): 2 个

### 分类分布

- **PATCH**: 21 threads (295 邮件)
- **RFC**: 3 threads (5 邮件)
- **Bug Report**: 2 threads (4 邮件)
- **Discussion**: 1 threads (2 邮件)

---

## 📌 PATCH

共 21 个 thread

---

### Thread 1: [PATCH v15 00/21] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs

**📧 邮件数**: 70 | **👥 参与者**: 7 | **📅 开始时间**: Thu, 17 Jul 2025 17:27:10 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 的补丁系列，主要目的是为非 CoCo 虚拟机启用主机用户空间映射的 guest_memfd 支持。补丁的主要内容包括：

1. **原始补丁/问题内容**：补丁系列（[PATCH v15 00/21]）旨在允许非 CoCo 虚拟机使用 guest_memfd 作为内存后端，简化内存管理，支持如 Firecracker 等虚拟机管理程序的使用场景。

2. **之前讨论要点**：历史讨论中，参与者们对补丁的多个方面进行了深入探讨，包括 Kconfig 选项的命名、功能的清晰性、以及如何处理不同类型虚拟机的内存支持等。特别是对 KVM 的内存管理机制进行了详细分析，强调了将 guest_memfd 支持扩展到非私有内存的重要性。

3. **本周的新讨论及进展**：本周的讨论集中在对补丁的具体实现和潜在问题上。Xiaoyao Li 提出了在 QEMU 中实现 mmap 支持的尝试，并讨论了与 TDX 虚拟机的兼容性问题。Fuad Tabba 和其他参与者明确表示不希望支持 TDX 中的 mmap 功能，认为这会引入复杂性。Sean Christopherson 进一步澄清了用户空间与 KVM 之间的内存映射关系，强调了 VMM 的责任，并提出了对未来支持的展望。整体上，参与者们对补丁的方向表示认可，并计划在后续版本中继续完善。

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
6. **[07-17 17:27]** [PATCH v15 10/21] KVM: x86/mmu: Generalize private_max_mapping_level
 x86 op to max_mapping_level
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[07-17 17:27]** [PATCH v15 11/21] KVM: x86/mmu: Allow NULL-able fault in kvm_max_private_mapping_level
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[07-17 17:27]** [PATCH v15 13/21] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[07-17 17:27]** [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default VM type
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[07-17 17:27]** [PATCH v15 16/21] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[07-17 17:27]** [PATCH v15 17/21] KVM: arm64: nv: Handle VNCR_EL2-triggered faults
 backed by guest_memfd
   - 发件人: Fuad Tabba <tabba@google.com>
12. **[07-17 17:27]** [PATCH v15 18/21] KVM: arm64: Enable host mapping of shared
 guest_memfd memory
   - 发件人: Fuad Tabba <tabba@google.com>
13. **[07-17 17:27]** [PATCH v15 19/21] KVM: Introduce the KVM capability KVM_CAP_GMEM_MMAP
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[07-18 09:42]** Re: [PATCH v15 03/21] KVM: Introduce kvm_arch_supports_gmem()
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
15. **[07-18 13:10]** Re: [PATCH v15 11/21] KVM: x86/mmu: Allow NULL-able fault in
 kvm_max_private_mapping_level
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
16. **[07-21 20:22]** Re: [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
17. **[07-21 13:41]** Re: [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: Fuad Tabba <tabba@google.com>
18. **[07-21 06:45]** Re: [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: Vishal Annapurve <vannapurve@google.com>
19. **[07-21 22:42]** Re: [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
20. **[07-21 07:42]** Re: [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: Sean Christopherson <seanjc@google.com>
21. **[07-21 07:47]** Re: [PATCH v15 03/21] KVM: Introduce kvm_arch_supports_gmem()
   - 发件人: Sean Christopherson <seanjc@google.com>
22. **[07-21 15:55]** Re: [PATCH v15 03/21] KVM: Introduce kvm_arch_supports_gmem()
   - 发件人: Fuad Tabba <tabba@google.com>
23. **[07-21 23:07]** Re: [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
24. **[07-21 08:17]** Re: [PATCH v15 01/21] KVM: Rename CONFIG_KVM_PRIVATE_MEM to CONFIG_KVM_GMEM
   - 发件人: Sean Christopherson <seanjc@google.com>
25. **[07-21 16:26]** Re: [PATCH v15 01/21] KVM: Rename CONFIG_KVM_PRIVATE_MEM to CONFIG_KVM_GMEM
   - 发件人: Fuad Tabba <tabba@google.com>
26. **[07-21 09:44]** Re: [PATCH v15 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Sean Christopherson <seanjc@google.com>
27. **[07-21 09:44]** Re: [PATCH v15 03/21] KVM: Introduce kvm_arch_supports_gmem()
   - 发件人: Sean Christopherson <seanjc@google.com>
28. **[07-21 09:45]** Re: [PATCH v15 04/21] KVM: x86: Introduce kvm->arch.supports_gmem
   - 发件人: Sean Christopherson <seanjc@google.com>
29. **[07-21 09:47]** Re: [PATCH v15 13/21] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Sean Christopherson <seanjc@google.com>
30. **[07-21 17:51]** Re: [PATCH v15 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Fuad Tabba <tabba@google.com>
31. **[07-21 17:56]** Re: [PATCH v15 13/21] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Fuad Tabba <tabba@google.com>
32. **[07-21 18:00]** Re: [PATCH v15 04/21] KVM: x86: Introduce kvm->arch.supports_gmem
   - 发件人: Fuad Tabba <tabba@google.com>
33. **[07-21 10:29]** Re: [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: Sean Christopherson <seanjc@google.com>
34. **[07-21 10:31]** Re: [PATCH v15 19/21] KVM: Introduce the KVM capability KVM_CAP_GMEM_MMAP
   - 发件人: Sean Christopherson <seanjc@google.com>
35. **[07-21 10:33]** Re: [PATCH v15 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Sean Christopherson <seanjc@google.com>
36. **[07-21 12:09]** Re: [PATCH v15 04/21] KVM: x86: Introduce kvm->arch.supports_gmem
   - 发件人: Sean Christopherson <seanjc@google.com>
37. **[07-21 12:46]** Re: [PATCH v15 10/21] KVM: x86/mmu: Generalize private_max_mapping_level
 x86 op to max_mapping_level
   - 发件人: Sean Christopherson <seanjc@google.com>
38. **[07-21 13:33]** Re: [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: Vishal Annapurve <vannapurve@google.com>
39. **[07-21 15:21]** Re: [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: Sean Christopherson <seanjc@google.com>
40. **[07-21 16:17]** Re: [PATCH v15 11/21] KVM: x86/mmu: Allow NULL-able fault in kvm_max_private_mapping_level
   - 发件人: Sean Christopherson <seanjc@google.com>
41. **[07-21 16:50]** Re: [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: Vishal Annapurve <vannapurve@google.com>
42. **[07-22 13:35]** Re: [PATCH v15 11/21] KVM: x86/mmu: Allow NULL-able fault in
 kvm_max_private_mapping_level
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
43. **[07-22 13:41]** Re: [PATCH v15 13/21] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
44. **[07-22 09:43]** Re: [PATCH v15 13/21] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Fuad Tabba <tabba@google.com>
45. **[07-22 17:25]** Re: [PATCH v15 15/21] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Kunwu Chan <kunwu.chan@linux.dev>
46. **[07-22 10:29]** Re: [PATCH v15 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Fuad Tabba <tabba@google.com>
47. **[07-22 11:35]** Re: [PATCH v15 11/21] KVM: x86/mmu: Allow NULL-able fault in kvm_max_private_mapping_level
   - 发件人: Fuad Tabba <tabba@google.com>
48. **[07-22 12:08]** Re: [PATCH v15 11/21] KVM: x86/mmu: Allow NULL-able fault in kvm_max_private_mapping_level
   - 发件人: Fuad Tabba <tabba@google.com>
49. **[07-22 20:31]** Re: [PATCH v15 16/21] KVM: arm64: Handle guest_memfd-backed guest
 page faults
   - 发件人: Kunwu Chan <kunwu.chan@linux.dev>
50. **[07-22 22:28]** Re: [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
51. **[07-22 07:32]** Re: [PATCH v15 11/21] KVM: x86/mmu: Allow NULL-able fault in kvm_max_private_mapping_level
   - 发件人: Sean Christopherson <seanjc@google.com>
52. **[07-22 07:35]** Re: [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: Sean Christopherson <seanjc@google.com>
53. **[07-22 07:37]** Re: [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: Sean Christopherson <seanjc@google.com>
54. **[07-22 16:30]** Re: [PATCH v15 11/21] KVM: x86/mmu: Allow NULL-able fault in kvm_max_private_mapping_level
   - 发件人: Fuad Tabba <tabba@google.com>
55. **[07-22 23:31]** Re: [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
56. **[07-22 17:50]** Re: [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: David Hildenbrand <david@redhat.com>
57. **[07-22 08:54]** Re: [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: Sean Christopherson <seanjc@google.com>
58. **[07-22 08:58]** Re: [PATCH v15 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Sean Christopherson <seanjc@google.com>
59. **[07-22 17:01]** Re: [PATCH v15 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Fuad Tabba <tabba@google.com>
60. **[07-22 16:42]** Re: [PATCH v15 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Sean Christopherson <seanjc@google.com>
61. **[07-23 09:20]** Re: [PATCH v15 16/21] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Marc Zyngier <maz@kernel.org>
62. **[07-23 09:26]** Re: [PATCH v15 16/21] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Marc Zyngier <maz@kernel.org>
63. **[07-23 09:29]** Re: [PATCH v15 17/21] KVM: arm64: nv: Handle VNCR_EL2-triggered faults backed by guest_memfd
   - 发件人: Marc Zyngier <maz@kernel.org>
64. **[07-23 09:33]** Re: [PATCH v15 18/21] KVM: arm64: Enable host mapping of shared guest_memfd memory
   - 发件人: Marc Zyngier <maz@kernel.org>
65. **[07-23 10:18]** Re: [PATCH v15 18/21] KVM: arm64: Enable host mapping of shared
 guest_memfd memory
   - 发件人: Fuad Tabba <tabba@google.com>
66. **[07-23 10:22]** Re: [PATCH v15 02/21] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Fuad Tabba <tabba@google.com>
67. **[07-23 19:44]** Re: [PATCH v15 16/21] KVM: arm64: Handle guest_memfd-backed guest
 page faults
   - 发件人: Kunwu Chan <kunwu.chan@linux.dev>
68. **[07-23 07:08]** Re: [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: Vishal Annapurve <vannapurve@google.com>
69. **[07-23 07:43]** Re: [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: Sean Christopherson <seanjc@google.com>
70. **[07-23 16:46]** Re: [PATCH v15 14/21] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: David Hildenbrand <david@redhat.com>

---

### Thread 2: [PATCH v16 00/22] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs

**📧 邮件数**: 60 | **👥 参与者**: 5 | **📅 开始时间**: Wed, 23 Jul 2025 11:46:52 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 的一系列补丁，主要集中在支持非 CoCo 虚拟机的 guest_memfd 相关功能上。以下是讨论的主要内容：

1. **原始补丁内容**：补丁系列旨在为非 CoCo 虚拟机启用 host 用户空间对 guest_memfd 支持的内存映射。此功能允许虚拟机监控器（VMM）如 Firecracker 完全使用 guest_memfd 支持的内存，从而简化内存管理并提高安全性。

2. **历史讨论要点**：之前的讨论主要集中在补丁的基础设施重构和 Kconfig 选项的清理上。补丁通过引入新的配置选项和重命名现有选项，使得对 guest_memfd 的支持更加清晰和一致。

3. **本周的新讨论与进展**：
   - 本周的讨论主要围绕补丁的具体实现和测试展开，包括对 KVM 的 mmap() 支持的增强。
   - 提出了多个补丁，涵盖了对 x86 和 arm64 架构的支持，确保 guest_memfd 的内存映射功能能够在不同的虚拟机类型下正常工作。
   - 讨论中还提到了一些代码的清理和重构，以提高可读性和可维护性。
   - 参与者对补丁进行了审查，并提出了一些建议和改进意见，最终达成共识，准备发布新的补丁版本。

总体而言，本周的讨论推动了 KVM 对 guest_memfd 支持的进一步完善，确保了在不同架构和虚拟机类型下的功能一致性与可靠性。

#### 📝 邮件列表

1. **[07-23 11:46]** [PATCH v16 00/22] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[07-23 11:46]** [PATCH v16 01/22] KVM: Rename CONFIG_KVM_PRIVATE_MEM to CONFIG_KVM_GUEST_MEMFD
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[07-23 11:46]** [PATCH v16 02/22] KVM: x86: Have all vendor neutral sub-configs
 depend on KVM_X86, not just KVM
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[07-23 11:46]** [PATCH v16 03/22] KVM: x86: Select KVM_GENERIC_PRIVATE_MEM directly
 from KVM_SW_PROTECTED_VM
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[07-23 11:46]** [PATCH v16 04/22] KVM: x86: Select TDX's KVM_GENERIC_xxx dependencies
 iff CONFIG_KVM_INTEL_TDX=y
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[07-23 11:46]** [PATCH v16 05/22] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_HAVE_KVM_ARCH_GMEM_POPULATE
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[07-23 11:46]** [PATCH v16 06/22] KVM: Rename kvm_slot_can_be_private() to kvm_slot_has_gmem()
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[07-23 11:46]** [PATCH v16 07/22] KVM: Fix comments that refer to slots_lock
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[07-23 11:47]** [PATCH v16 08/22] KVM: Fix comment that refers to kvm uapi header path
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[07-23 11:47]** [PATCH v16 09/22] KVM: x86: Enable KVM_GUEST_MEMFD for all 64-bit builds
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[07-23 11:47]** [PATCH v16 10/22] KVM: guest_memfd: Add plumbing to host to map
 guest_memfd pages
   - 发件人: Fuad Tabba <tabba@google.com>
12. **[07-23 11:47]** [PATCH v16 11/22] KVM: guest_memfd: Track guest_memfd mmap support in memslot
   - 发件人: Fuad Tabba <tabba@google.com>
13. **[07-23 11:47]** [PATCH v16 12/22] KVM: x86/mmu: Rename .private_max_mapping_level()
 to .gmem_max_mapping_level()
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[07-23 11:47]** [PATCH v16 13/22] KVM: x86/mmu: Hoist guest_memfd max level/order
 helpers "up" in mmu.c
   - 发件人: Fuad Tabba <tabba@google.com>
15. **[07-23 11:47]** [PATCH v16 14/22] KVM: x86/mmu: Enforce guest_memfd's max order when
 recovering hugepages
   - 发件人: Fuad Tabba <tabba@google.com>
16. **[07-23 11:47]** [PATCH v16 15/22] KVM: x86/mmu: Extend guest_memfd's max mapping
 level to shared mappings
   - 发件人: Fuad Tabba <tabba@google.com>
17. **[07-23 11:47]** [PATCH v16 16/22] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
18. **[07-23 11:47]** [PATCH v16 17/22] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Fuad Tabba <tabba@google.com>
19. **[07-23 11:47]** [PATCH v16 18/22] KVM: arm64: nv: Handle VNCR_EL2-triggered faults
 backed by guest_memfd
   - 发件人: Fuad Tabba <tabba@google.com>
20. **[07-23 11:47]** [PATCH v16 19/22] KVM: arm64: Enable support for guest_memfd backed memory
   - 发件人: Fuad Tabba <tabba@google.com>
21. **[07-23 11:47]** [PATCH v16 20/22] KVM: Allow and advertise support for host mmap() on
 guest_memfd files
   - 发件人: Fuad Tabba <tabba@google.com>
22. **[07-23 11:47]** [PATCH v16 21/22] KVM: selftests: Do not use hardcoded page sizes in
 guest_memfd test
   - 发件人: Fuad Tabba <tabba@google.com>
23. **[07-23 11:47]** [PATCH v16 22/22] KVM: selftests: guest_memfd mmap() test when mmap
 is supported
   - 发件人: Fuad Tabba <tabba@google.com>
24. **[07-23 21:06]** Re: [PATCH v16 02/22] KVM: x86: Have all vendor neutral sub-configs
 depend on KVM_X86, not just KVM
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
25. **[07-23 15:13]** Re: [PATCH v16 02/22] KVM: x86: Have all vendor neutral sub-configs
 depend on KVM_X86, not just KVM
   - 发件人: David Hildenbrand <david@redhat.com>
26. **[07-23 15:13]** Re: [PATCH v16 03/22] KVM: x86: Select KVM_GENERIC_PRIVATE_MEM
 directly from KVM_SW_PROTECTED_VM
   - 发件人: David Hildenbrand <david@redhat.com>
27. **[07-23 15:14]** Re: [PATCH v16 04/22] KVM: x86: Select TDX's KVM_GENERIC_xxx
 dependencies iff CONFIG_KVM_INTEL_TDX=y
   - 发件人: David Hildenbrand <david@redhat.com>
28. **[07-23 15:17]** Re: [PATCH v16 09/22] KVM: x86: Enable KVM_GUEST_MEMFD for all 64-bit
 builds
   - 发件人: David Hildenbrand <david@redhat.com>
29. **[07-23 21:17]** Re: [PATCH v16 03/22] KVM: x86: Select KVM_GENERIC_PRIVATE_MEM
 directly from KVM_SW_PROTECTED_VM
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
30. **[07-23 21:22]** Re: [PATCH v16 04/22] KVM: x86: Select TDX's KVM_GENERIC_xxx
 dependencies iff CONFIG_KVM_INTEL_TDX=y
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
31. **[07-23 21:27]** Re: [PATCH v16 05/22] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to
 CONFIG_HAVE_KVM_ARCH_GMEM_POPULATE
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
32. **[07-23 21:42]** Re: [PATCH v16 09/22] KVM: x86: Enable KVM_GUEST_MEMFD for all 64-bit
 builds
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
33. **[07-23 21:51]** Re: [PATCH v16 13/22] KVM: x86/mmu: Hoist guest_memfd max level/order
 helpers "up" in mmu.c
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
34. **[07-23 21:55]** Re: [PATCH v16 14/22] KVM: x86/mmu: Enforce guest_memfd's max order
 when recovering hugepages
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
35. **[07-23 22:03]** Re: [PATCH v16 10/22] KVM: guest_memfd: Add plumbing to host to map
 guest_memfd pages
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
36. **[07-24 15:15]** Re: [PATCH v16 22/22] KVM: selftests: guest_memfd mmap() test when
 mmap is supported
   - 发件人: Sean Christopherson <seanjc@google.com>
37. **[07-24 15:32]** Re: [PATCH v16 14/22] KVM: x86/mmu: Enforce guest_memfd's max order
 when recovering hugepages
   - 发件人: Sean Christopherson <seanjc@google.com>
38. **[07-24 15:33]** Re: [PATCH v16 10/22] KVM: guest_memfd: Add plumbing to host to map
 guest_memfd pages
   - 发件人: Sean Christopherson <seanjc@google.com>
39. **[07-24 15:35]** Re: [PATCH v16 04/22] KVM: x86: Select TDX's KVM_GENERIC_xxx
 dependencies iff CONFIG_KVM_INTEL_TDX=y
   - 发件人: Sean Christopherson <seanjc@google.com>
40. **[07-24 15:41]** Re: [PATCH v16 05/22] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_HAVE_KVM_ARCH_GMEM_POPULATE
   - 发件人: Sean Christopherson <seanjc@google.com>
41. **[07-24 15:44]** Re: [PATCH v16 00/22] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs
   - 发件人: Sean Christopherson <seanjc@google.com>
42. **[07-24 16:03]** Re: [PATCH v16 13/22] KVM: x86/mmu: Hoist guest_memfd max level/order
 helpers "up" in mmu.c
   - 发件人: Ackerley Tng <ackerleytng@google.com>
43. **[07-24 16:04]** Re: [PATCH v16 13/22] KVM: x86/mmu: Hoist guest_memfd max level/order
 helpers "up" in mmu.c
   - 发件人: Ackerley Tng <ackerleytng@google.com>
44. **[07-24 16:21]** Re: [PATCH v16 14/22] KVM: x86/mmu: Enforce guest_memfd's max order
 when recovering hugepages
   - 发件人: Ackerley Tng <ackerleytng@google.com>
45. **[07-24 16:31]** Re: [PATCH v16 15/22] KVM: x86/mmu: Extend guest_memfd's max mapping
 level to shared mappings
   - 发件人: Ackerley Tng <ackerleytng@google.com>
46. **[07-24 16:34]** Re: [PATCH v16 14/22] KVM: x86/mmu: Enforce guest_memfd's max order
 when recovering hugepages
   - 发件人: Ackerley Tng <ackerleytng@google.com>
47. **[07-24 16:46]** Re: [PATCH v16 00/22] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs
   - 发件人: Ackerley Tng <ackerleytng@google.com>
48. **[07-25 06:53]** Re: [PATCH v16 15/22] KVM: x86/mmu: Extend guest_memfd's max mapping
 level to shared mappings
   - 发件人: Sean Christopherson <seanjc@google.com>
49. **[07-25 07:31]** Re: [PATCH v16 14/22] KVM: x86/mmu: Enforce guest_memfd's max order
 when recovering hugepages
   - 发件人: Sean Christopherson <seanjc@google.com>
50. **[07-25 07:56]** Re: [PATCH v16 00/22] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs
   - 发件人: Sean Christopherson <seanjc@google.com>
51. **[07-25 23:13]** Re: [PATCH v16 05/22] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to
 CONFIG_HAVE_KVM_ARCH_GMEM_POPULATE
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
52. **[07-25 09:40]** Re: [PATCH v16 15/22] KVM: x86/mmu: Extend guest_memfd's max mapping
 level to shared mappings
   - 发件人: Ackerley Tng <ackerleytng@google.com>
53. **[07-25 10:13]** Re: [PATCH v16 15/22] KVM: x86/mmu: Extend guest_memfd's max mapping
 level to shared mappings
   - 发件人: Sean Christopherson <seanjc@google.com>
54. **[07-25 10:24]** Re: [PATCH v16 14/22] KVM: x86/mmu: Enforce guest_memfd's max order
 when recovering hugepages
   - 发件人: Sean Christopherson <seanjc@google.com>
55. **[07-25 12:16]** Re: [PATCH v16 14/22] KVM: x86/mmu: Enforce guest_memfd's max order
 when recovering hugepages
   - 发件人: Ackerley Tng <ackerleytng@google.com>
56. **[07-25 12:34]** Re: [PATCH v16 15/22] KVM: x86/mmu: Extend guest_memfd's max mapping
 level to shared mappings
   - 发件人: Ackerley Tng <ackerleytng@google.com>
57. **[07-25 12:52]** Re: [PATCH v16 15/22] KVM: x86/mmu: Extend guest_memfd's max mapping
 level to shared mappings
   - 发件人: Sean Christopherson <seanjc@google.com>
58. **[07-25 14:31]** Re: [PATCH v16 15/22] KVM: x86/mmu: Extend guest_memfd's max mapping
 level to shared mappings
   - 发件人: Ackerley Tng <ackerleytng@google.com>
59. **[07-25 15:01]** Re: [PATCH v16 15/22] KVM: x86/mmu: Extend guest_memfd's max mapping
 level to shared mappings
   - 发件人: Sean Christopherson <seanjc@google.com>
60. **[07-25 15:25]** Re: [PATCH v16 15/22] KVM: x86/mmu: Extend guest_memfd's max mapping
 level to shared mappings
   - 发件人: Ackerley Tng <ackerleytng@google.com>

---

### Thread 3: [PATCH 0/7] KVM: arm64: FEAT_RASv1p1 support and RAS selection

**📧 邮件数**: 15 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 21 Jul 2025 11:19:48 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM（Kernel-based Virtual Machine）中支持 ARM64 架构的 RASv1p1 特性及其选择。Marc Zyngier 提出了一个包含七个补丁的系列，旨在解决与 RAS（Reliability, Availability, and Serviceability）相关的问题。

**原始补丁/问题内容**：
补丁的主要目标是实现对 RASv1p1 特性的支持，允许在不实现复杂功能的情况下，仍然向虚拟机提供架构合规的外观。补丁包括对 RAS 寄存器的处理、HCR_EL2 配置的过滤、以及在未广告 RAS 时将寄存器设置为 UNDEF。

**之前讨论要点**：
在历史讨论中，Marc 提到在调试 RAS 相关问题时，发现测试环境实现了 RASv1p1，但在向来宾广告该特性时存在问题。讨论中还提到了一些与 HCR_EL2 配置相关的复杂性，以及如何处理 RAS 寄存器访问。

**本周的新讨论、进展或结论**：
本周的讨论集中在补丁的具体实现上，Marc 提出了多个补丁的详细内容，包括如何处理 RASv1p1 寄存器、过滤 HCR_EL2 位、以及在未广告 RAS 时的寄存器访问处理。Cornelia Huck 和其他参与者对补丁提出了反馈和建议，Marc 也表示将根据反馈进行修改和完善。整体来看，补丁系列得到了积极的认可，并计划在后续版本中继续推进。

#### 📝 邮件列表

1. **[07-21 11:19]** [PATCH 0/7] KVM: arm64: FEAT_RASv1p1 support and RAS selection
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-21 11:19]** [PATCH 1/7] arm64: Add capability denoting FEAT_RASv1p1
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[07-21 11:19]** [PATCH 2/7] KVM: arm64: Filter out HCR_EL2 bits when running in hypervisor context
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[07-21 11:19]** [PATCH 3/7] KVM: arm64: Make RAS registers UNDEF when RAS isn't advertised
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[07-21 11:19]** [PATCH 4/7] KVM: arm64: Handle RASv1p1 registers
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[07-21 11:19]** [PATCH 5/7] KVM: arm64: Ignore HCR_EL2.FIEN set by L1 guest's EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[07-21 11:19]** [PATCH 6/7] KVM: arm64: Expose FEAT_RASv1p1 in a canonical manner
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[07-21 11:19]** [PATCH 7/7] KVM: arm64: Make ID_AA64PFR0_EL1.RAS writable
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[07-21 14:32]** Re: [PATCH 6/7] KVM: arm64: Expose FEAT_RASv1p1 in a canonical manner
   - 发件人: Cornelia Huck <cohuck@redhat.com>
10. **[07-21 13:55]** Re: [PATCH 6/7] KVM: arm64: Expose FEAT_RASv1p1 in a canonical manner
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[07-21 14:08]** Re: [PATCH 4/7] KVM: arm64: Handle RASv1p1 registers
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[07-21 15:12]** Re: [PATCH 6/7] KVM: arm64: Expose FEAT_RASv1p1 in a canonical manner
   - 发件人: Cornelia Huck <cohuck@redhat.com>
13. **[07-21 14:33]** Re: [PATCH 6/7] KVM: arm64: Expose FEAT_RASv1p1 in a canonical manner
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[07-21 14:52]** Re: [PATCH 1/7] arm64: Add capability denoting FEAT_RASv1p1
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
15. **[07-21 15:24]** Re: (subset) [PATCH 0/7] KVM: arm64: FEAT_RASv1p1 support and RAS selection
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 4: [PATCH v3 00/13] stackleak: Support Clang stack depth tracking

**📧 邮件数**: 14 | **👥 参与者**: 5 | **📅 开始时间**: Thu, 17 Jul 2025 16:25:05 -0700

#### 🤖 AI 总结

本邮件线程讨论的主题是关于支持 Clang 堆栈深度跟踪的补丁系列，主要集中在对现有代码的改进和重命名。补丁系列的核心内容是将原有的 STACKLEAK 功能重命名为 KSTACK_ERASE，并引入新的配置选项，以便更好地支持 Clang 的堆栈深度回调。

在历史讨论中，Kees Cook 提出了多个补丁，旨在优化与 KCOV 相关的代码，特别是处理 __init 和 inline 函数之间的差异。讨论中提到，GCC 的内联逻辑较为脆弱，可能会影响函数的内联决策，导致某些函数未按预期内联。参与者们对如何处理这些问题进行了深入探讨，并提出了不同的解决方案。

在本周的新讨论中，Will Deacon 和其他参与者对 Kees 提出的补丁进行了反馈，讨论了不同的实现方法。Will 提出了一种更稳健的处理方式，但 Kees 更倾向于保持小范围的修复，以避免引入新的复杂性。Nicolas Schier 也指出了在补丁中遗漏的配置文件，并对其进行了修正。整体来看，讨论集中在如何平衡代码的稳定性与功能扩展之间，最终达成了继续小规模修复的共识。

#### 📝 邮件列表

1. **[07-17 16:25]** [PATCH v3 00/13] stackleak: Support Clang stack depth tracking
   - 发件人: Kees Cook <kees@kernel.org>
2. **[07-17 16:25]** [PATCH v3 01/13] stackleak: Rename STACKLEAK to KSTACK_ERASE
   - 发件人: Kees Cook <kees@kernel.org>
3. **[07-17 16:25]** [PATCH v3 04/13] x86: Handle KCOV __init vs inline mismatches
   - 发件人: Kees Cook <kees@kernel.org>
4. **[07-18 11:36]** Re: [PATCH v3 04/13] x86: Handle KCOV __init vs inline mismatches
   - 发件人: Mike Rapoport <rppt@kernel.org>
5. **[07-18 15:51]** Re: [PATCH v3 04/13] x86: Handle KCOV __init vs inline mismatches
   - 发件人: Kees Cook <kees@kernel.org>
6. **[07-20 16:10]** Re: [PATCH v3 04/13] x86: Handle KCOV __init vs inline mismatches
   - 发件人: Ard Biesheuvel <ardb@kernel.org>
7. **[07-21 13:47]** Re: [PATCH v3 04/13] x86: Handle KCOV __init vs inline mismatches
   - 发件人: Will Deacon <will@kernel.org>
8. **[07-21 22:02]** Re: [PATCH v3 01/13] stackleak: Rename STACKLEAK to KSTACK_ERASE
   - 发件人: Nicolas Schier <nicolas.schier@linux.dev>
9. **[07-21 13:14]** Re: [PATCH v3 04/13] x86: Handle KCOV __init vs inline mismatches
   - 发件人: Kees Cook <kees@kernel.org>
10. **[07-21 13:16]** Re: [PATCH v3 01/13] stackleak: Rename STACKLEAK to KSTACK_ERASE
   - 发件人: Kees Cook <kees@kernel.org>
11. **[07-21 13:49]** Re: [PATCH v3 04/13] x86: Handle KCOV __init vs inline mismatches
   - 发件人: Kees Cook <kees@kernel.org>
12. **[07-22 16:55]** Re: [PATCH v3 04/13] x86: Handle KCOV __init vs inline mismatches
   - 发件人: Ard Biesheuvel <ardb@kernel.org>
13. **[07-22 11:26]** Re: [PATCH v3 04/13] x86: Handle KCOV __init vs inline mismatches
   - 发件人: Mike Rapoport <rppt@kernel.org>
14. **[07-22 14:29]** Re: [PATCH v3 04/13] x86: Handle KCOV __init vs inline mismatches
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 5: [PATCH kvmtool v2 0/6] arm64: Nested virtualization support

**📧 邮件数**: 13 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 25 Jul 2025 15:40:54 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的嵌套虚拟化支持的补丁系列（[PATCH kvmtool v2 0/6]）。该补丁系列的主要目标是增强 KVM 工具对 ARM64 嵌套虚拟化的支持，确保其能够在主线内核中正常工作。

在历史讨论中，补丁的背景和目的得到了阐述，强调了嵌套虚拟化在 ARMv8.3 架构中的重要性。补丁包括更新内核头文件、引入新的命令行选项以支持在 EL2 启动 VCPU、设置维护中断等功能。

本周的新讨论中，参与者 Andre Przywara 提交了补丁的多个版本，详细介绍了每个补丁的功能。补丁 1 同步了内核 UAPI 头文件，补丁 2 引入了嵌套虚拟化的初步支持，补丁 3 允许设置维护中断，补丁 4 和 5 则分别增加了计数器偏移控制和 FEAT_E2H0 支持。Marc Zyngier 对补丁的描述提出了建议，强调了用户界面的简洁性和功能的清晰性。

总体而言，本周的讨论集中在补丁的细节和实现上，确保嵌套虚拟化功能的顺利集成和用户友好性。

#### 📝 邮件列表

1. **[07-25 15:40]** [PATCH kvmtool v2 0/6] arm64: Nested virtualization support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
2. **[07-25 15:40]** [PATCH kvmtool v2 1/6] Sync kernel UAPI headers with v6.16-rc1
   - 发件人: Andre Przywara <andre.przywara@arm.com>
3. **[07-25 15:40]** [PATCH kvmtool v2 2/6] arm64: Initial nested virt support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
4. **[07-25 15:40]** [PATCH kvmtool v2 3/6] arm64: nested: add support for setting maintenance IRQ
   - 发件人: Andre Przywara <andre.przywara@arm.com>
5. **[07-25 15:40]** [PATCH kvmtool v2 4/6] arm64: Add counter offset control
   - 发件人: Andre Przywara <andre.przywara@arm.com>
6. **[07-25 15:40]** [PATCH kvmtool v2 5/6] arm64: add FEAT_E2H0 support (TBC)
   - 发件人: Andre Przywara <andre.przywara@arm.com>
7. **[07-25 15:41]** [PATCH kvmtool v2 6/6] arm64: Generate HYP timer interrupt specifiers
   - 发件人: Andre Przywara <andre.przywara@arm.com>
8. **[07-25 17:37]** Re: [PATCH kvmtool v2 5/6] arm64: add FEAT_E2H0 support (TBC)
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[07-26 17:01]** Re: [PATCH kvmtool v2 5/6] arm64: add FEAT_E2H0 support (TBC)
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
10. **[07-26 10:19]** Re: [PATCH kvmtool v2 5/6] arm64: add FEAT_E2H0 support (TBC)
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[07-26 10:25]** Re: [PATCH kvmtool v2 4/6] arm64: Add counter offset control
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[07-26 18:11]** Re: [PATCH kvmtool v2 5/6] arm64: add FEAT_E2H0 support (TBC)
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
13. **[07-26 11:34]** Re: [PATCH kvmtool v2 5/6] arm64: add FEAT_E2H0 support (TBC)
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 6: [PATCH v4 0/6] KVM: arm64: Allow userspace to write GICD_TYPER2.nASSGIcap

**📧 邮件数**: 13 | **👥 参与者**: 2 | **📅 开始时间**: Wed,  9 Jul 2025 14:14:11 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁系列，主要目的是允许用户空间写入 GICD_TYPER2.nASSGIcap 寄存器。

1. **原始补丁内容**：Oliver Upton 提出的补丁系列（PATCH v4 0/6）旨在允许用户空间在初始化 VGIC（虚拟通用中断控制器）之前修改 GICD_TYPER2 寄存器的值，以便更好地支持虚拟化环境中的中断管理。

2. **之前讨论要点**：在历史讨论中，参与者对多个补丁进行了审查和反馈，主要集中在补丁的实现细节和潜在的错误修复上。例如，Eric Auger 提出了一些关于代码可读性和逻辑一致性的建议，并对补丁的功能进行了确认和评论。

3. **本周的新讨论与进展**：本周的讨论主要围绕补丁的细节进行，Oliver 对 Eric 的反馈进行了回应，确认了一些设计选择的合理性，并表示将根据建议调整补丁文档。Eric 还提出了对文档内容的修改建议，认为不应给用户空间过多的控制权，避免造成误解。

总体来看，本周的讨论进一步明确了补丁的实现细节和文档内容，确保了补丁在功能和文档上的一致性。

#### 📝 邮件列表

1. **[07-09 14:14]** [PATCH v4 0/6] KVM: arm64: Allow userspace to write GICD_TYPER2.nASSGIcap
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-09 14:14]** [PATCH v4 1/6] KVM: arm64: Disambiguate support for vSGIs v. vLPIs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[07-09 14:14]** [PATCH v4 2/6] KVM: arm64: vgic-v3: Consolidate MAINT_IRQ handling
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[07-09 14:14]** [PATCH v4 3/6] KVM: arm64: vgic-v3: Allow access to GICD_IIDR prior to initialization
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[07-09 14:14]** [PATCH v4 6/6] Documentation: KVM: arm64: Describe VGICv3 registers writable pre-init
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[07-14 12:20]** Re: [PATCH v4 1/6] KVM: arm64: Disambiguate support for vSGIs v.
 vLPIs
   - 发件人: Eric Auger <eauger@redhat.com>
7. **[07-14 14:52]** Re: [PATCH v4 2/6] KVM: arm64: vgic-v3: Consolidate MAINT_IRQ
 handling
   - 发件人: Eric Auger <eauger@redhat.com>
8. **[07-14 16:41]** Re: [PATCH v4 3/6] KVM: arm64: vgic-v3: Allow access to GICD_IIDR
 prior to initialization
   - 发件人: Eric Auger <eauger@redhat.com>
9. **[07-14 17:06]** Re: [PATCH v4 6/6] Documentation: KVM: arm64: Describe VGICv3
 registers writable pre-init
   - 发件人: Eric Auger <eauger@redhat.com>
10. **[07-22 14:36]** Re: [PATCH v4 1/6] KVM: arm64: Disambiguate support for vSGIs v.
 vLPIs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[07-22 14:42]** Re: [PATCH v4 2/6] KVM: arm64: vgic-v3: Consolidate MAINT_IRQ
 handling
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
12. **[07-22 14:47]** Re: [PATCH v4 3/6] KVM: arm64: vgic-v3: Allow access to GICD_IIDR
 prior to initialization
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[07-22 14:50]** Re: [PATCH v4 6/6] Documentation: KVM: arm64: Describe VGICv3
 registers writable pre-init
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 7: [PATCH v5 00/12] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 13 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 21 Jul 2025 14:04:54 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 Armv8.8 SPE（Statistical Profiling Extension）特性的补丁集，主要包括对新过滤功能的支持。

1. **原始补丁内容**：
   本次补丁集（[PATCH v5 00/12]）旨在支持三项新 SPE 特性：FEAT_SPEv1p4 过滤器、FEAT_SPE_EFT 扩展过滤和 SPE_FEAT_FDS 数据源过滤。每项特性均可独立应用。

2. **之前讨论要点**：
   该补丁集的历史版本（v4、v3 等）中，开发者对特性进行了多次修改和优化，包括对寄存器的更新、文档的扩展以及对过滤器的实现方式进行了重构。讨论中强调了与旧版 Perf 工具的兼容性和新配置字段的必要性。

3. **本周的新讨论与进展**：
   本周的讨论集中在补丁的具体实现上，包括：
   - 新增的 PMSFCR_EL1 和 PMSDSFR_EL1 寄存器字段。
   - 支持 FEAT_SPEv1p4 过滤器的实现。
   - 引入了用于数据源过滤的 inv_data_src_filter。
   - 更新了 perf_event_attr 结构以支持新的 config4 字段。
   - 文档中增加了对新特性的描述，确保用户能够理解如何使用这些新功能。

整体来看，本周的讨论和补丁更新主要集中在增强 Arm SPE 的功能和用户体验上，确保新特性能够被有效利用。

#### 📝 邮件列表

1. **[07-21 14:04]** [PATCH v5 00/12] perf: arm_spe: Armv8.8 SPE features
   - 发件人: James Clark <james.clark@linaro.org>
2. **[07-21 14:04]** [PATCH v5 01/12] arm64: sysreg: Add new PMSFCR_EL1 fields and
 PMSDSFR_EL1 register
   - 发件人: James Clark <james.clark@linaro.org>
3. **[07-21 14:04]** [PATCH v5 02/12] perf: arm_spe: Support FEAT_SPEv1p4 filters
   - 发件人: James Clark <james.clark@linaro.org>
4. **[07-21 14:04]** [PATCH v5 03/12] perf: arm_spe: Expose event filter
   - 发件人: James Clark <james.clark@linaro.org>
5. **[07-21 14:04]** [PATCH v5 04/12] perf: arm_spe: Add support for FEAT_SPE_EFT
 extended filtering
   - 发件人: James Clark <james.clark@linaro.org>
6. **[07-21 14:04]** [PATCH v5 05/12] arm64/boot: Factor out a macro to check SPE
 version
   - 发件人: James Clark <james.clark@linaro.org>
7. **[07-21 14:05]** [PATCH v5 06/12] arm64/boot: Enable EL2 requirements for
 SPE_FEAT_FDS
   - 发件人: James Clark <james.clark@linaro.org>
8. **[07-21 14:05]** [PATCH v5 07/12] KVM: arm64: Add trap configs for PMSDSFR_EL1
   - 发件人: James Clark <james.clark@linaro.org>
9. **[07-21 14:05]** [PATCH v5 08/12] perf: Add perf_event_attr::config4
   - 发件人: James Clark <james.clark@linaro.org>
10. **[07-21 14:05]** [PATCH v5 09/12] perf: arm_spe: Add support for filtering on data
 source
   - 发件人: James Clark <james.clark@linaro.org>
11. **[07-21 14:05]** [PATCH v5 10/12] tools headers UAPI: Sync linux/perf_event.h with
 the kernel sources
   - 发件人: James Clark <james.clark@linaro.org>
12. **[07-21 14:05]** [PATCH v5 11/12] perf tools: Add support for
 perf_event_attr::config4
   - 发件人: James Clark <james.clark@linaro.org>
13. **[07-21 14:05]** [PATCH v5 12/12] perf docs: arm-spe: Document new SPE filtering
 features
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 8: [PATCH v4 00/12] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 13 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 21 Jul 2025 13:53:31 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于支持 Armv8.8 SPE（Statistical Profiling Extension）新特性的补丁系列，共包含12个补丁。主要新增了三个特性：FEAT_SPEv1p4 过滤器、FEAT_SPE_EFT 扩展过滤和 SPE_FEAT_FDS 数据源过滤。

在历史讨论中，补丁的背景是为了增强 Linux 内核对 Arm 架构中 SPE 的支持，特别是通过新的过滤机制来提高性能监控的灵活性和精确度。之前的讨论集中在如何实现这些特性，以及它们与现有性能监控工具的兼容性。

本周的新讨论中，James Clark 提出了多个补丁，详细介绍了每个特性的实现细节。例如，FEAT_SPEv1p4 允许使用新的过滤位，FEAT_SPE_EFT 引入了对现有过滤器的掩码位支持，而 SPE_FEAT_FDS 则允许基于数据源进行过滤。补丁还包括对相关系统寄存器的修改、性能工具的更新以及文档的补充，以确保用户能够理解和使用这些新特性。

总的来说，本周的讨论和补丁进展表明，Linux 内核在支持 Arm 架构的性能监控方面正在不断增强，尤其是在新特性和工具的兼容性方面。

#### 📝 邮件列表

1. **[07-21 13:53]** [PATCH v4 00/12] perf: arm_spe: Armv8.8 SPE features
   - 发件人: James Clark <james.clark@linaro.org>
2. **[07-21 13:53]** [PATCH v4 01/12] arm64: sysreg: Add new PMSFCR_EL1 fields and
 PMSDSFR_EL1 register
   - 发件人: James Clark <james.clark@linaro.org>
3. **[07-21 13:53]** [PATCH v4 02/12] perf: arm_spe: Support FEAT_SPEv1p4 filters
   - 发件人: James Clark <james.clark@linaro.org>
4. **[07-21 13:53]** [PATCH v4 03/12] perf: arm_spe: Expose event filter
   - 发件人: James Clark <james.clark@linaro.org>
5. **[07-21 13:53]** [PATCH v4 04/12] perf: arm_spe: Add support for FEAT_SPE_EFT
 extended filtering
   - 发件人: James Clark <james.clark@linaro.org>
6. **[07-21 13:53]** [PATCH v4 05/12] arm64/boot: Factor out a macro to check SPE
 version
   - 发件人: James Clark <james.clark@linaro.org>
7. **[07-21 13:53]** [PATCH v4 06/12] arm64/boot: Enable EL2 requirements for
 SPE_FEAT_FDS
   - 发件人: James Clark <james.clark@linaro.org>
8. **[07-21 13:53]** [PATCH v4 07/12] KVM: arm64: Add trap configs for PMSDSFR_EL1
   - 发件人: James Clark <james.clark@linaro.org>
9. **[07-21 13:53]** [PATCH v4 08/12] perf: Add perf_event_attr::config4
   - 发件人: James Clark <james.clark@linaro.org>
10. **[07-21 13:53]** [PATCH v4 09/12] perf: arm_spe: Add support for filtering on data
 source
   - 发件人: James Clark <james.clark@linaro.org>
11. **[07-21 13:53]** [PATCH v4 10/12] tools headers UAPI: Sync linux/perf_event.h with
 the kernel sources
   - 发件人: James Clark <james.clark@linaro.org>
12. **[07-21 13:53]** [PATCH v4 11/12] perf tools: Add support for
 perf_event_attr::config4
   - 发件人: James Clark <james.clark@linaro.org>
13. **[07-21 13:53]** [PATCH v4 12/12] perf docs: arm-spe: Document new SPE filtering
 features
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 9: [PATCH 0/4] KVM: arm64: Userspace GICv3 sysreg access fixes and testing

**📧 邮件数**: 12 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 18 Jul 2025 12:11:50 +0100

#### 🤖 AI 总结

本邮件讨论主题为“[PATCH 0/4] KVM: arm64: Userspace GICv3 sysreg access fixes and testing”，主要围绕修复和测试 KVM 中 GICv3 系统寄存器的用户空间访问问题。

历史讨论中，Marc Zyngier 提出了四个补丁。第一个补丁修正了 ICH_HCR_EL2 在系统寄存器表中的错误排序，确保可以从用户空间访问。第二个补丁澄清了 `check_sysreg_table()` 中的重置回调检查，第三个补丁则强制要求 GICv3 系统寄存器表的排序，以避免未来的错误。最后一个补丁增加了一个自测，确保 GICv3 系统寄存器的可用性。

在本周的新讨论中，Itaru Kitayama 报告了在 RevC FVP 上对补丁的测试结果，确认了自测的运行情况。尽管他提到了一些跳过的测试项，Marc Zyngier 对此表示困惑，并询问问题的来源。Sebastian Ott 对前三个补丁进行了审核并表示通过，确认了这些补丁的有效性。

总体来看，本周的讨论主要集中在补丁的测试结果和审核反馈上，显示出对 GICv3 系统寄存器访问修复工作的积极进展。

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
6. **[07-23 14:00]** Re: [PATCH 4/4] KVM: arm64: selftest: vgic-v3: Add basic GICv3
 sysreg userspace access test
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>
7. **[07-23 09:15]** Re: [PATCH 4/4] KVM: arm64: selftest: vgic-v3: Add basic GICv3 sysreg userspace access test
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[07-23 17:46]** Re: [PATCH 4/4] KVM: arm64: selftest: vgic-v3: Add basic GICv3 sysreg
 userspace access test
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>
9. **[07-23 17:38]** Re: [PATCH 1/4] KVM: arm64: vgic-v3: Fix ordering of ICH_HCR_EL2
   - 发件人: Sebastian Ott <sebott@redhat.com>
10. **[07-23 17:38]** Re: [PATCH 2/4] KVM: arm64: Clarify the check for reset callback in
 check_sysreg_table()
   - 发件人: Sebastian Ott <sebott@redhat.com>
11. **[07-23 17:40]** Re: [PATCH 3/4] KVM: arm64: Enforce the sorting of the GICv3 system
 register table
   - 发件人: Sebastian Ott <sebott@redhat.com>
12. **[07-23 17:56]** Re: [PATCH 4/4] KVM: arm64: selftest: vgic-v3: Add basic GICv3 sysreg
 userspace access test
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

### Thread 10: [PATCH v7 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler

**📧 邮件数**: 11 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 7 Jul 2025 17:06:23 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下使用 SMCCC 1.2 进行 FF-A（Firmware Framework for Arm）初始化及主机处理的补丁（PATCH v7 2/5）。该补丁旨在确保在处理 FF-A 调用时，遵循 SMCCC 1.2 规范，特别是关于未使用参数寄存器的处理。

在历史讨论中，参与者们主要集中在如何正确解读 SMCCC 和 FF-A 规范，确保在调用中将未使用的寄存器清零，以符合规范要求。讨论中提到，EL2 代理应依赖 EL3 正确处理参数，而不是逐个调用进行不同处理。

本周的新讨论中，Per Larsen 指出使用原始调用的函数 ID 可能在某些情况下无法正确工作，尤其是在处理不同位宽的响应时。Will Deacon 认为不检查源 ID 是一个潜在的漏洞，可能导致安全问题，建议在未来的补丁中修复。此外，讨论还涉及到是否应将 FF-A 驱动更新以支持新的 64 位 FFA_RUN 调用，参与者们一致认为应与规范作者协调，以确保驱动与规范的一致性。

总体而言，本周的讨论进一步深化了对补丁的理解，并提出了未来改进的方向，包括安全性和兼容性问题的解决。

#### 📝 邮件列表

1. **[07-07 17:06]** Re: [PATCH v7 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen <perl@immunant.com>
2. **[07-18 14:37]** Re: [PATCH v7 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Will Deacon <will@kernel.org>
3. **[07-18 14:53]** Re: [PATCH v7 5/5] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Will Deacon <will@kernel.org>
4. **[07-18 22:54]** Re: [PATCH v7 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen <perl@immunant.com>
5. **[07-21 04:01]** Re: [PATCH v7 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: =?UTF-8?B?QXJ2ZSBIasO4bm5ldsOlZw==?= <arve@android.com>
6. **[07-21 04:13]** Re: [PATCH v7 5/5] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: =?UTF-8?B?QXJ2ZSBIasO4bm5ldsOlZw==?= <arve@android.com>
7. **[07-21 15:43]** Re: [PATCH v7 5/5] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Per Larsen <perl@immunant.com>
8. **[07-21 17:20]** Re: [PATCH v7 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen <perl@immunant.com>
9. **[07-22 16:03]** Re: [PATCH v7 5/5] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Will Deacon <will@kernel.org>
10. **[07-22 16:55]** Re: [PATCH v7 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Will Deacon <will@kernel.org>
11. **[07-22 17:37]** Re: [PATCH v7 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>

---

### Thread 11: [PATCH v5 0/6] KVM: arm64: Allow userspace to write GICD_TYPER2.nASSGIcap

**📧 邮件数**: 10 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 23 Jul 2025 23:27:59 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下允许用户空间写入 GICD_TYPER2.nASSGIcap 的补丁（PATCH v5 0/6）。该补丁的主要目的是允许用户在虚拟机创建之前配置该特性，以便在资源有限的环境中控制虚拟处理器（vPE）的分配。

在历史讨论中，补丁的版本更新主要集中在修复一些小问题和明确补丁日志中的细微变化。参与者对补丁的内容进行了多次审查，确保其符合设计要求。

本周的新讨论中，Oliver Upton 提出了多个补丁，涵盖了对 VGICv3 的支持、对 GICD_IIDR 的访问控制以及对 GICD_TYPER2.nASSGIcap 的写入权限。Raghavendra Rao Ananta 进一步讨论了如何将 vLPI 和 vSGI 的支持捆绑在一起，以确保用户空间能够正确控制 vPE 的分配。最后，Marc Zyngier 对补丁进行了审核并表示支持。

总体而言，本周的讨论集中在补丁的具体实现和潜在的设计问题上，确保了功能的正确性和稳定性。

#### 📝 邮件列表

1. **[07-23 23:27]** [PATCH v5 0/6] KVM: arm64: Allow userspace to write GICD_TYPER2.nASSGIcap
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-23 23:28]** [PATCH v5 1/6] KVM: arm64: Disambiguate support for vSGIs v. vLPIs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[07-23 23:28]** [PATCH v5 2/6] KVM: arm64: vgic-v3: Consolidate MAINT_IRQ handling
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[07-23 23:28]** [PATCH v5 3/6] KVM: arm64: vgic-v3: Allow access to GICD_IIDR prior to initialization
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[07-23 23:28]** [PATCH v5 4/6] KVM: arm64: vgic-v3: Allow userspace to write GICD_TYPER2.nASSGIcap
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[07-23 23:28]** [PATCH v5 5/6] KVM: arm64: selftests: Add test for nASSGIcap attribute
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[07-23 23:28]** [PATCH v5 6/6] Documentation: KVM: arm64: Describe VGICv3 registers writable pre-init
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[07-25 17:55]** Re: [PATCH v5 0/6] KVM: arm64: Allow userspace to write GICD_TYPER2.nASSGIcap
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[07-25 15:53]** Re: [PATCH v5 4/6] KVM: arm64: vgic-v3: Allow userspace to write GICD_TYPER2.nASSGIcap
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
10. **[07-26 08:45]** Re: [PATCH v5 4/6] KVM: arm64: vgic-v3: Allow userspace to write
 GICD_TYPER2.nASSGIcap
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 12: [resend][PATCH 1/2] arm64: kvm: sys_regs: use string choices helper

**📧 邮件数**: 10 | **👥 参与者**: 4 | **📅 开始时间**: Fri, 18 Jul 2025 01:50:24 +0000

#### 🤖 AI 总结

本邮件线程讨论了两个主要的补丁（patch），旨在优化 ARM64 架构下 KVM 的系统寄存器和页面表处理。

**原始补丁内容**：
第一个补丁（PATCH 1/2）提议在 `arm64: kvm: sys_regs` 中使用字符串选择助手，以简化代码。第二个补丁（PATCH 2/2）则在 `arm64: kvm: trace_handle_exit` 中同样应用了字符串选择助手。

**之前讨论要点**：
在历史讨论中，Kuninori Morimoto 提出了这两个补丁，并获得了积极反馈，认为这种方法可以提升代码的可读性和维护性。

**本周新讨论及进展**：
本周的讨论中，Oliver Upton 确认这两个补丁已被应用到下一版本中，表示感谢。此外，Raghavendra Rao Ananta 提出了两个新的补丁，旨在解决在销毁大型虚拟机时可能出现的调度警告问题。他的补丁将 `kvm_pgtable_stage2_destroy()` 函数拆分为两个部分，以便在处理大页表时能更好地进行调度。Sean Christopherson 对第二个补丁的描述提出了建议，认为应更明确地表达其目的。整体来看，本周的讨论集中在补丁的应用和新优化方案的提出上，推动了 KVM 的进一步改进。

#### 📝 邮件列表

1. **[07-18 01:50]** [resend][PATCH 1/2] arm64: kvm: sys_regs: use string choices helper
   - 发件人: Kuninori Morimoto <kuninori.morimoto.gx@renesas.com>
2. **[07-18 01:50]** [resend][PATCH 2/2] arm64: kvm: trace_handle_exit: use string choices helper
   - 发件人: Kuninori Morimoto <kuninori.morimoto.gx@renesas.com>
3. **[07-23 23:49]** Re: [resend][PATCH 1/2] arm64: kvm: sys_regs: use string choices helper
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[07-23 23:49]** Re: [resend][PATCH 2/2] arm64: kvm: trace_handle_exit: use string choices helper
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[07-23 23:49]** Re: [PATCH 0/2] KVM: arm64: Fixes and clarifications for FEAT_S1POE
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[07-24 23:51]** [PATCH 0/2] KVM: arm64: Destroy the stage-2 page-table periodically
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
7. **[07-24 23:51]** [PATCH 1/2] KVM: arm64: Split kvm_pgtable_stage2_destroy()
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
8. **[07-24 23:51]** [PATCH 2/2] KVM: arm64: Destroy the stage-2 page-table periodically
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
9. **[07-25 07:59]** Re: [PATCH 2/2] KVM: arm64: Destroy the stage-2 page-table periodically
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[07-25 09:22]** Re: [PATCH 2/2] KVM: arm64: Destroy the stage-2 page-table periodically
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>

---

### Thread 13: [PATCH 6.1.y] KVM: arm64: silence -Wuninitialized-const-pointer warning

**📧 邮件数**: 8 | **👥 参与者**: 4 | **📅 开始时间**: Thu, 24 Jul 2025 18:15:28 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 KVM（内核虚拟机）在 arm64 架构下的补丁，目的是消除 Clang 22 编译器发出的未初始化常量指针的警告。补丁的具体内容是通过初始化 `struct sys_reg_desc clidr` 来解决这个警告。

在历史讨论中，补丁的提出者 Justin Stitt 指出，`get_clidr_el1()` 函数并不关心 `clidr` 的常量性，因为它会在使用时去掉常量属性，因此该警告并不影响功能。然而，Marc Zyngier 认为这个补丁只是掩盖了设计上的问题，并建议应回溯修复相关的系列补丁，以改善 6.1 版本的内核质量。

在本周的新讨论中，参与者们对补丁的必要性和有效性进行了深入探讨。Greg KH 提出，既然 Clang 22 并不是 6.1.y 树的支持编译器，是否有必要为此做出修正。Nathan Chancellor 认为，虽然当前的警告是由于函数参数的常量性引起的，但可以考虑在特定情况下禁用该警告。总体来看，讨论中存在对补丁有效性的质疑，且补丁的维护者似乎对该补丁并不热衷，可能会选择暂时忽略这个问题。

#### 📝 邮件列表

1. **[07-24 18:15]** [PATCH 6.1.y] KVM: arm64: silence -Wuninitialized-const-pointer warning
   - 发件人: Justin Stitt <justinstitt@google.com>
2. **[07-24 18:19]** Re: [PATCH 6.1.y] KVM: arm64: silence -Wuninitialized-const-pointer
 warning
   - 发件人: Justin Stitt <justinstitt@google.com>
3. **[07-25 08:30]** Re: [PATCH 6.1.y] KVM: arm64: silence -Wuninitialized-const-pointer warning
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[07-25 10:58]** Re: [PATCH 6.1.y] KVM: arm64: silence -Wuninitialized-const-pointer
 warning
   - 发件人: Greg KH <gregkh@linuxfoundation.org>
5. **[07-25 09:26]** Re: [PATCH 6.1.y] KVM: arm64: silence -Wuninitialized-const-pointer
 warning
   - 发件人: Nathan Chancellor <nathan@kernel.org>
6. **[07-25 09:38]** Re: [PATCH 6.1.y] KVM: arm64: silence -Wuninitialized-const-pointer
 warning
   - 发件人: Nathan Chancellor <nathan@kernel.org>
7. **[07-25 17:53]** Re: [PATCH 6.1.y] KVM: arm64: silence -Wuninitialized-const-pointer warning
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[07-25 19:08]** Re: [PATCH 6.1.y] KVM: arm64: silence -Wuninitialized-const-pointer
 warning
   - 发件人: Greg KH <gregkh@linuxfoundation.org>

---

### Thread 14: [PATCH v5 0/5] support FEAT_LSUI and apply it on futex atomic ops

**📧 邮件数**: 8 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 22 Jul 2025 13:19:51 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于支持 Armv9.6 的 FEAT_LSUI 特性，并将其应用于 futex 原子操作的补丁集（PATCH v5 0/5）。该补丁集的主要内容包括：

1. **原始补丁内容**：补丁集旨在支持 FEAT_LSUI 特性，使得内核在访问用户内存时无需清除 PSTATE.PAN 位。补丁包括五个部分：添加 FEAT_LSUI 的 CPU 特性、将其暴露给虚拟机、添加 Kconfig 配置、重构原有的 futex 原子操作实现，以及支持使用 FEAT_LSUI 的 futex 原子操作。

2. **历史讨论要点**：补丁经历了多个版本的修改，主要集中在代码结构的调整和对虚拟机的支持上。每个版本都对补丁进行了重组和优化，以确保其兼容性和功能性。

3. **本周的新讨论与进展**：本周的讨论主要集中在补丁的审查和反馈上。参与者 Marc Zyngier 提出应给予更多时间进行审查，并建议推迟提交到下一个合并窗口，以便作者能更仔细地打磨补丁。Yeoreum Yun 对此表示感谢并承认自己的急躁。

总体而言，本周的讨论强调了补丁的审查过程和作者对反馈的重视，同时也反映出对新特性集成的谨慎态度。

#### 📝 邮件列表

1. **[07-22 13:19]** [PATCH v5 0/5] support FEAT_LSUI and apply it on futex atomic ops
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[07-22 13:19]** [PATCH v5 1/5] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[07-22 13:19]** [PATCH v5 2/5] KVM: arm64: expose FEAT_LSUI to guest
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[07-22 13:19]** [PATCH v5 3/5] arm64: Kconfig: add LSUI Kconfig
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[07-22 13:19]** [PATCH v5 4/5] arm64: futex: refactor futex atomic operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
6. **[07-22 13:19]** [PATCH v5 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
7. **[07-22 15:53]** Re: [PATCH v5 0/5] support FEAT_LSUI and apply it on futex atomic ops
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[07-22 17:19]** Re: [PATCH v5 0/5] support FEAT_LSUI and apply it on futex atomic ops
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 15: [PATCH] arm64: kvm, smccc: Fix vendor uuid

**📧 邮件数**: 7 | **👥 参与者**: 5 | **📅 开始时间**: Mon, 21 Jul 2025 14:05:58 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于修复 ARM64 架构下 KVM 的 SMCCC（安全多处理器调用标准）中的供应商 UUID 问题。Jack Thomson 提出的补丁旨在解决在之前的提交中引入的字节序问题，导致生成的 UUID 与旧版本不匹配，从而影响与旧版来宾内核的兼容性，并导致某些设备（如 PTP）无法在来宾中使用。

在之前的讨论中，参与者们指出该问题的严重性，并强调需要尽快解决，以确保在即将发布的 6.16 版本中修复此错误。Marc Zyngier 和 Sudeep Holla 等人对补丁表示认可，并提供了测试和审查支持。

在本周的新讨论中，Jack Thomson 提到补丁已被应用到 arm64 的修复分支中。Will Deacon 表示感谢，并对之前未能测试旧内核的情况表示歉意。整体来看，参与者们对补丁的修复表示赞同，并积极推动其尽快合并，以恢复与旧内核的兼容性。

#### 📝 邮件列表

1. **[07-21 14:05]** [PATCH] arm64: kvm, smccc: Fix vendor uuid
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
2. **[07-21 16:59]** Re: [PATCH] arm64: kvm, smccc: Fix vendor uuid
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[07-21 17:15]** Re: [PATCH] arm64: kvm, smccc: Fix vendor uuid
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>
4. **[07-21 18:14]** Re: [PATCH] arm64: kvm, smccc: Fix vendor uuid
   - 发件人: Will Deacon <will@kernel.org>
5. **[07-21 10:20]** Re: [PATCH] arm64: kvm, smccc: Fix vendor uuid
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
6. **[07-21 10:27]** Re: [PATCH] arm64: kvm, smccc: Fix vendor uuid
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
7. **[07-21 18:45]** Re: [PATCH] arm64: kvm, smccc: Fix vendor uuid
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 16: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 11 Jul 2025 12:39:50 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 ARM64 架构下处理 SEA（系统错误异常）的补丁（PATCH v2 1/6）。该补丁旨在实现虚拟机退出到用户空间，以更优雅地处理 SEA，尤其是在缺乏 APEI（高级平台错误接口）支持的情况下。

在历史讨论中，参与者 Oliver Upton 和 Jiaqi Yan 进行了多次交流，探讨了补丁的细节和改进建议。Oliver 提出了一些关于代码结构和错误处理的建议，强调在处理阶段-1 和阶段-2 描述符时的不同情况，并讨论了如何避免将真实的阶段-2 外部中止暴露给用户空间。Jiaqi 表示会根据这些反馈更新补丁，并考虑将当前的补丁集拆分为两个部分，以便更好地管理和提交。

在本周的新讨论中，Jiaqi 提到他的 v3 版本已经准备好，并希望确认最佳的提交选项。他强调了即使在新 ARM64 平台上，KVM 仍然是处理 SEA 的关键，因此希望尽快与上游社区达成一致，以锁定提议的方法和用户空间 API（UAPI）。

总体而言，讨论集中在补丁的细节、改进建议以及如何更好地与社区合作以推动补丁的进展。

#### 📝 邮件列表

1. **[07-11 12:39]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-11 16:59]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
3. **[07-12 12:57]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[07-19 14:24]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
5. **[07-25 15:54]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>

---

### Thread 17: [PATCH 0/5] KVM: arm64: Config driven dependencies for TCR2/SCTLR/MDCR

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 14 Jul 2025 12:54:58 +0100

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的配置驱动依赖性，主要涉及 TCR2、SCTLR 和 MDCR 寄存器的处理。Marc Zyngier 提出了一个包含五个补丁的系列，目的是将这些寄存器转换为配置驱动的清理框架，以提高代码的整洁性和可维护性。这些补丁在 2025 年 7 月 14 日被提交，并于 7 月 16 日被 Oliver Upton 确认应用于下一个开发版本。

在历史讨论中，Oliver Upton 提到已成功将补丁应用于项目中，并提供了每个补丁的链接，显示出对该系列补丁的支持和认可。

本周的新讨论中，Vlastimil Babka 报告了一个合并提交导致的文件冲突问题，并指出该问题是由于本地残留文件引起的。Oliver Upton 对此表示感谢，并承诺在重建合并历史时会修正该问题，以便顺利发送拉取请求。这表明在补丁应用后，团队仍在积极处理合并过程中的问题，以确保代码库的稳定性和一致性。

#### 📝 邮件列表

1. **[07-14 12:54]** [PATCH 0/5] KVM: arm64: Config driven dependencies for TCR2/SCTLR/MDCR
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-16 09:47]** Re: [PATCH 0/5] KVM: arm64: Config driven dependencies for TCR2/SCTLR/MDCR
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[07-23 17:53]** Re: [PATCH 0/5] KVM: arm64: Config driven dependencies for
 TCR2/SCTLR/MDCR
   - 发件人: Vlastimil Babka <vbabka@suse.cz>
4. **[07-23 23:51]** Re: [PATCH 0/5] KVM: arm64: Config driven dependencies for
 TCR2/SCTLR/MDCR
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 18: [PATCH] KVM: arm64: selftest: Add standalone test checking for KVM's own UUID

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 21 Jul 2025 16:51:36 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的自测试补丁，旨在增加一个独立的测试，以检查 KVM 的 UUID（通用唯一标识符）。Marc Zyngier 提出了这个补丁，指出 UUID 的处理可能会出现问题，因此需要一个自测试来及时发现这些问题。

在历史讨论中，补丁的主要内容是添加一个新的自测试文件 `kvm-uuid.c`，该文件通过调用 KVM 的 UUID 相关功能，验证返回的值是否符合预期。补丁还修改了 `Makefile.kvm` 以包含新的测试程序。

在本周的新讨论中，Andrew Jones 提出了对补丁的建议，询问是否应该检查返回值 `res.a0` 是否等于 `SMCCC_RET_SUCCESS`，并建议创建一个通用的 ucall 帮助函数，以简化类似的测试模式。Sebastian Ott 对补丁进行了审核并表示支持。Marc Zyngier 对 Andrew 的建议表示认可，指出当前的 KVM 自测试代码大多是针对 x86 的，自己并不打算对此进行修改。

总体来看，本周的讨论集中在补丁的细节和潜在的改进上，参与者们积极交流，推动了补丁的进展。

#### 📝 邮件列表

1. **[07-21 16:51]** [PATCH] KVM: arm64: selftest: Add standalone test checking for KVM's own UUID
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-22 11:18]** Re: [PATCH] KVM: arm64: selftest: Add standalone test checking for
 KVM's own UUID
   - 发件人: Andrew Jones <ajones@ventanamicro.com>
3. **[07-22 16:39]** Re: [PATCH] KVM: arm64: selftest: Add standalone test checking for
 KVM's own UUID
   - 发件人: Sebastian Ott <sebott@redhat.com>
4. **[07-22 16:47]** Re: [PATCH] KVM: arm64: selftest: Add standalone test checking for KVM's own UUID
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 19: [PATCH v9 34/43] arm64: RME: Propagate number of breakpoints and
 watchpoints to userspace

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 24 Jul 2025 11:20:47 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM64 架构的补丁（PATCH v9 34/43），其主要目的是将断点和观察点的数量传递给用户空间。这一补丁旨在改善调试功能，使用户能够更好地管理和利用硬件调试资源。

在之前的讨论中，虽然没有详细记录，但可以推测该补丁是为了支持 ARM64 架构中的 RME（Runtime Memory Encryption）特性，确保用户空间能够获取到硬件支持的断点和观察点的数量。这一功能对于开发和调试 ARM64 应用程序至关重要。

在本周的新讨论中，参与者 Joey Gouly 对该补丁进行了审核，并表示支持，标记为“Reviewed-by”。这表明该补丁得到了认可，可能会在后续版本中被合并。此外，Joey Gouly 还对另一个相关补丁（PATCH v9 36/43）进行了同样的审核，显示出对整个系列补丁的积极反馈。

总体来看，本周的进展表明该补丁在审核过程中获得了支持，推动了 ARM64 RME 特性的进一步实现。

#### 📝 邮件列表

1. **[07-24 11:20]** Re: [PATCH v9 34/43] arm64: RME: Propagate number of breakpoints and
 watchpoints to userspace
   - 发件人: Joey Gouly <joey.gouly@arm.com>
2. **[07-24 11:47]** Re: [PATCH v9 36/43] arm64: RME: Initialize PMCR.N with number
 counter supported by RMM
   - 发件人: Joey Gouly <joey.gouly@arm.com>

---

### Thread 20: [PATCH] KVM: arm64: Check for SYSREGS_ON_CPU before accessing the CPU state

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Sun, 20 Jul 2025 11:22:29 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，主要内容是检查在访问 CPU 状态之前是否加载了系统寄存器（SYSREGS_ON_CPU）。

在历史讨论中，Marc Zyngier 提出了该补丁，指出由于承诺在不加载 vcpu 的情况下使异常可见，导致外部中止自测失败。经过调查发现，当前代码在 VHE（Virtualization Host Extensions）模式下存在问题，因为在此时并未检查系统寄存器是否已加载。为了解决这一问题，补丁增加了必要的检查，并强调了这一检查的绝对必要性。

在本周的新讨论中，Oliver Upton 回复确认已将该补丁应用到下一步开发中，并表示感谢。这表明该补丁得到了认可并将继续推进。

总结而言，该补丁旨在修复 KVM 在 arm64 架构下的一个关键问题，历史讨论提供了背景信息，而本周的进展则显示出补丁已被采纳。

#### 📝 邮件列表

1. **[07-20 11:22]** [PATCH] KVM: arm64: Check for SYSREGS_ON_CPU before accessing the CPU state
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-21 15:24]** Re: [PATCH] KVM: arm64: Check for SYSREGS_ON_CPU before accessing the CPU state
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 21: [PATCH v4 01/23] arm64: cpufeature: Add cpucap for HPMN0

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 21 Jul 2025 18:00:34 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构的补丁（PATCH v4 01/23），其内容是为 HPMN0 添加 CPU 特性标志（cpucap）。该补丁旨在增强 ARM64 的 CPU 功能识别。

在本周的新讨论中，参与者 Colton Lewis 对之前的审查表示感谢，并确认将根据审查意见进行修改。邮件中提到的审查者是 Suzuki K Poulose，虽然没有详细列出审查的具体内容，但可以推测审查涉及补丁的实现细节和潜在改进。

总结来说，本周的讨论主要集中在补丁的修改和完善上，Colton Lewis 表示将根据反馈进行调整，显示出对审查过程的重视和对补丁质量的追求。

#### 📝 邮件列表

1. **[07-21 18:00]** Re: [PATCH v4 01/23] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Colton Lewis <coltonlewis@google.com>

---

## 📌 RFC

共 3 个 thread

---

### Thread 1: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 25 Jul 2025 15:31:05 +0530

#### 🤖 AI 总结

本邮件线程讨论了一个名为“[RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests”的补丁集，旨在为 KVM（内核虚拟机）启用嵌套虚拟化的自测试功能。

在历史讨论中，Marc Zyngier询问Ganapatrao Kulkarni，是否认为这些补丁在不支持裸金属 hypervisor 的情况下仍然有价值，或者是否需要先重构以支持递归客户机。

本周的新讨论中，Ganapatrao Kulkarni对补丁的实现提出了批评，认为当前的测试方法不够合理。他指出，现有测试应专注于在 EL2（异常级别2）下运行，而不是嵌套虚拟化。他建议去掉补丁中与“嵌套”相关的内容，专注于 EL2 的两种实现方式。此外，他强调，EL2 测试不应是可选的，若 EL2 可用，测试应自动运行，而不应依赖于选项。他对补丁的进展表示担忧，认为在过去几个月中没有足够的进展来确保必要的嵌套虚拟化测试能够完成。

总的来说，本周的讨论集中在补丁的合理性和必要性上，特别是如何更有效地实现 EL2 测试。

#### 📝 邮件列表

1. **[07-25 15:31]** Re: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
2. **[07-25 11:59]** Re: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [RFC PATCH 2/2] KVM: arm64: vgic-its: Unmap all vPEs on shutdown

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 22 Jul 2025 15:46:29 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 vgic-its（虚拟通用中断控制器）的一个补丁，主要内容是提出在系统关闭时解除所有虚拟处理单元（vPEs）的映射。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的背景是为了优化在系统关闭时的资源管理，确保 vPEs 不再占用内存资源。参与者 Oliver Upton 和 David Woodhouse 在本周的新讨论中进一步探讨了补丁的实现细节和潜在问题。

本周的讨论主要集中在以下几点：Oliver 提到在解除 vPE 映射之前，需要确保 vPEs 已被从 redistributors 中移除，以避免消耗不确定的 vPE 状态。同时，他提到在未来的 KHO（Kernel Hypervisor Optimization）中，可能实现不必将所有 vCPUs 下线的 kexec 操作，这样可以提高效率。David 也指出当前 GIC（通用中断控制器）在被静默时仍然访问内存的问题，并提到这一问题不仅影响 KVM 主机，也影响到来宾系统的休眠过程。

总体而言，本周的讨论深化了对补丁实施的理解，并提出了对未来改进的期望。

#### 📝 邮件列表

1. **[07-22 15:46]** Re: [RFC PATCH 2/2] KVM: arm64: vgic-its: Unmap all vPEs on shutdown
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-23 11:42]** Re: [RFC PATCH 2/2] KVM: arm64: vgic-its: Unmap all vPEs on shutdown
   - 发件人: David Woodhouse <dwmw2@infradead.org>

---

### Thread 3: [RFC PATCH 2/2] KVM: arm64: vgic-its: Unmap all vPEs on shutdown

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Jul 2025 12:35:40 +0200

#### 🤖 AI 总结

本邮件主题为“[RFC PATCH 2/2] KVM: arm64: vgic-its: Unmap all vPEs on shutdown”，主要讨论了在 KVM 的 arm64 架构中，关闭虚拟机时如何处理虚拟处理单元（vPEs）的解除映射问题。

在历史讨论中，尚未有具体的补丁或讨论记录，因此没有相关的背景信息提供。

在本周的新讨论中，参与者 David Woodhouse 提出了对该补丁的关注，询问是否有关于操作系统在正确关闭通用中断控制器（GIC）时的具体期望。他希望能获得来自 Arm 的指导，以确保在关闭虚拟机时能够正确地处理 GIC 的状态。

总结来看，目前该补丁的具体内容和背景尚不明确，但参与者对如何正确实现这一功能表现出浓厚的兴趣，并寻求进一步的技术支持和指导。

#### 📝 邮件列表

1. **[07-22 12:35]** Re: [RFC PATCH 2/2] KVM: arm64: vgic-its: Unmap all vPEs on shutdown
   - 发件人: David Woodhouse <dwmw2@infradead.org>

---

## 📌 Bug Report

共 2 个 thread

---

### Thread 1: [Bug Report] external_aborts failure related to efa1368ba9f4 ("KVM:
 arm64: Commit exceptions from KVM_SET_VCPU_EVENTS immediately")

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 21 Jul 2025 07:00:00 -0700

#### 🤖 AI 总结

本邮件线程讨论了与 KVM (Kernel-based Virtual Machine) 相关的一个 bug 报告，具体是关于提交 efa1368ba9f4 ("KVM: arm64: Commit exceptions from KVM_SET_VCPU_EVENTS immediately") 引发的 external_aborts 测试失败问题。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该提交可能影响了 KVM 的异常处理机制，导致在执行某些自测试时出现问题。

本周的新讨论中，参与者 Jiaqi Yan 报告了在进行 SEA (Synchronous Exception Acknowledgment) 注入开发时，发现 tools/testing/selftests/kvm/arm64/external_aborts.c 测试失败。具体表现为寄存器中的程序计数器（PC）值不符合预期。Jiaqi 发现，当回退提交 efa1368ba9f4 后，所有测试均通过，表明该提交可能存在缺陷。Jiaqi 请求原作者 Oliver 对此问题进行检查，并在后续邮件中再次提醒。

最后，Marc Zyngier 也参与了讨论，提供了相关的 Git 提交链接，可能是为了进一步分析和解决该问题。整体来看，当前的讨论集中在定位和解决因最近提交引发的测试失败问题上。

#### 📝 邮件列表

1. **[07-21 07:00]** [Bug Report] external_aborts failure related to efa1368ba9f4 ("KVM:
 arm64: Commit exceptions from KVM_SET_VCPU_EVENTS immediately")
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
2. **[07-25 15:38]** Re: [Bug Report] external_aborts failure related to efa1368ba9f4
 ("KVM: arm64: Commit exceptions from KVM_SET_VCPU_EVENTS immediately")
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
3. **[07-26 10:18]** Re: [Bug Report] external_aborts failure related to efa1368ba9f4
 ("KVM: arm64: Commit exceptions from KVM_SET_VCPU_EVENTS immediately")
   - 发件人: Marc Zyngier <maz@misterjones.org>

---

### Thread 2: [bug report] KVM: arm64: Add a range to __pkvm_host_unshare_guest()

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Jul 2025 13:59:06 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个 bug 报告，具体涉及到 `__pkvm_host_unshare_guest()` 函数的修复。

1. **原始问题**：在使用透明大页（transparent huge pages）启动 pkvm 客户机时，出现了内核崩溃，错误信息显示在 `arch/arm64/kvm/hyp/nvhe/mem_protect.c` 的第 1088 行。崩溃的原因是 `pkvm_pgtable_stage_relax_perms()` 函数在处理块映射时，假设了页面大小，导致了不一致的状态检查。

2. **之前的讨论**：由于本邮件线程没有历史讨论，无法提供之前的讨论要点。

3. **本周的新讨论**：本周，参与者 Ben Horgan 提出了一个补丁，修复了上述问题。补丁的主要修改是调整了 `assert_host_shared_guest()` 的调用，将页面大小参数改为 0，以适应不同的映射情况。应用此补丁后，Ben 表示不再遇到崩溃问题，并提供了相关的错误日志和调用栈信息，确认了修复的有效性。

总的来说，本周的讨论集中在解决 KVM 在特定条件下的崩溃问题，并通过补丁实现了成功修复。

#### 📝 邮件列表

1. **[07-22 13:59]** [bug report] KVM: arm64: Add a range to __pkvm_host_unshare_guest()
   - 发件人: Ben Horgan <ben.horgan@arm.com>

---

## 📌 Discussion

共 1 个 thread

---

### Thread 1: KVM: arm64: vgic-its: Return -ENXIO to invalid
 KVM_DEV_ARM_VGIC_GRP_CTRL attrs

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 22 Jul 2025 12:33:52 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 vgic-its（虚拟通用中断控制器）相关的一个补丁。该补丁的内容是当遇到无效的 KVM_DEV_ARM_VGIC_GRP_CTRL 属性时，返回 -ENXIO 错误码，以增强错误处理的准确性。

在之前的讨论中，David Woodhouse 提出了这个补丁，并在邮件中询问是否有进一步的反馈或进展，但没有收到回复。

在本周的新讨论中，David Woodhouse 再次发出提醒，询问补丁的状态。随后，Oliver Upton 回复表示该补丁已被应用到下一个版本中，并提供了补丁的链接。这表明该补丁得到了认可并将进入后续的开发流程。

总结来看，本周的讨论主要集中在补丁的应用确认上，标志着这一改进措施的推进，旨在提升 KVM 在处理无效属性时的稳定性和可靠性。

#### 📝 邮件列表

1. **[07-22 12:33]** Re: KVM: arm64: vgic-its: Return -ENXIO to invalid
 KVM_DEV_ARM_VGIC_GRP_CTRL attrs
   - 发件人: David Woodhouse <dwmw2@infradead.org>
2. **[07-23 23:49]** Re: KVM: arm64: vgic-its: Return -ENXIO to invalid KVM_DEV_ARM_VGIC_GRP_CTRL attrs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

