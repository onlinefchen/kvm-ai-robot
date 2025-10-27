# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 11:36:09

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

本邮件线程讨论了一个针对 KVM 的补丁系列，主要目的是为非 CoCo 虚拟机启用主机用户空间映射的 guest_memfd 支持。补丁系列的核心在于允许 KVM 使用 guest_memfd 作为内存后端，简化内存管理并支持多种虚拟机场景。

**历史讨论要点**：
最初的补丁（PATCH v15 00/21）提出了对 KVM 的一系列改进，包括去除对 KVM_SW_PROTECTED_VM 的依赖、重命名 Kconfig 选项以更准确地反映其功能，以及引入新的函数以支持 guest_memfd 的架构兼容性。这些补丁旨在扩展 KVM 对 guest_memfd 的支持，使其不仅限于私有内存，还包括共享内存。

**本周新讨论**：
本周的讨论集中在补丁 v15 14/21 上，参与者探讨了在 TDX 虚拟机中是否应支持使用 mmap 的 guest_memfd。Xiaoyao Li 提出，QEMU 可以在不传递 guest_memfd 的情况下使用 mmap，但在 TDX 中却因 kvm_arch_supports_gmem_mmap() 返回 false 而失败。Fuad Tabba 表示不希望支持此功能，因为 TDX 使用了不同的内存管理范式。其他参与者讨论了 KVM 是否需要在创建内存槽时强制检查用户空间地址与 guest_memfd 的一致性，最终达成一致认为不应强制执行此检查，因这会影响性能。

总的来说，邮件讨论围绕着如何在 KVM 中更好地支持 guest_memfd 及其在不同虚拟机类型中的应用展开，强调了设计的灵活性与性能之间的权衡。

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

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）的补丁系列，主要集中在为非 CoCo 虚拟机启用基于 guest_memfd 的内存的主机用户空间映射。

1. **原始补丁内容**：
   该补丁系列（PATCH v16 00/22）旨在为非 CoCo 虚拟机启用基于 guest_memfd 的内存映射，主要包括对 Kconfig 选择和依赖关系的重构，确保在 KVM x86 和 arm64 上始终启用 guest_memfd。这一功能支持多种 KVM 使用场景，如 Firecracker 虚拟机的运行、增强安全性以及为 CoCo 平台的受限 mmap() 支持奠定基础。

2. **历史讨论要点**：
   之前的讨论集中在如何清晰地重命名和组织 Kconfig 选项，以避免对 "私有" 内存的误解，并确保补丁系列的逻辑清晰。补丁还涉及到对现有基础设施的重构，以便更好地支持未来的功能扩展。

3. **本周的新讨论与进展**：
   本周的讨论主要围绕补丁的具体实现和测试，包括对 guest_memfd 的 mmap() 支持的实现细节。参与者们讨论了如何处理不同虚拟机类型的内存映射、如何确保内存的安全性，以及如何在自测中验证新功能的有效性。补丁的多个版本经过审查，最终达成一致，准备发布最终版本（v17）。此外，补丁还扩展了自测用例，以确保对 guest_memfd 的 mmap 功能进行全面测试。

总体而言，本周的讨论推动了 KVM 在内存管理方面的进展，特别是在支持基于 guest_memfd 的内存映射方面，确保了更高的安全性和灵活性。

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

本邮件线程讨论了针对 KVM（内核虚拟机）在 arm64 架构中支持 RASv1p1（可靠性、可用性和可服务性）特性的补丁系列。Marc Zyngier 提出了七个补丁，旨在解决与 RAS 相关的问题，并确保虚拟机能够正确处理 RASv1p1 特性。

在历史讨论中，Marc 指出当前的实现存在问题，例如在未实现 RASv1p1 的情况下仍然向虚拟机广告该特性，导致访问 RASv1p1 寄存器时出现错误。补丁的目标是降低 RAS 支持的复杂性，同时保持架构合规性。

本周的新讨论中，Marc 提交了补丁并详细说明了每个补丁的功能，包括：
1. 添加 RASv1p1 能力的检测。
2. 在运行在虚拟机上下文中时过滤 HCR_EL2 的某些位。
3. 当未广告 RAS 时，将 RAS 寄存器设置为 UNDEF。
4. 处理 RASv1p1 寄存器的访问。
5. 忽略由 L1 客户机设置的 HCR_EL2.FIEN。
6. 以规范方式向客户机展示 RASv1p1。
7. 使 ID_AA64PFR0_EL1.RAS 可写，以便在不同 RAS 支持的系统间恢复虚拟机。

讨论中还涉及了补丁的细节和潜在的语义差异，参与者对补丁的内容表示认可，并提出了一些改进建议。整体上，补丁系列的目标是提升 KVM 在 arm64 上的 RAS 支持能力。

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

本邮件线程讨论了一个关于 Linux 内核的补丁系列，主题为“stackleak: 支持 Clang 堆栈深度跟踪”。该补丁系列的主要目的是将现有的 GCC 插件替换为 Clang 实现，以增强堆栈深度跟踪的能力。

在历史讨论中，Kees Cook 提出了多个补丁，包括将 `STACKLEAK` 重命名为 `KSTACK_ERASE`，以便为 Clang 的堆栈深度回调支持做准备。此外，还讨论了在 x86 架构下处理 KCOV 的 `__init` 与内联函数不匹配的问题，强调了 GCC 的内联逻辑的脆弱性。

在本周的新讨论中，参与者们对补丁进行了进一步的审查和反馈。Will Deacon 提出了一个更稳健的处理方法，Kees Cook 则表示他尝试过该方法，但效果不佳，决定坚持小范围的修复。此外，Nicolas Schier 指出在补丁中遗漏了对 `arch/loongarch/Kconfig` 的更新，Kees Cook 也对此表示感谢并确认了修复。

总体来看，本周的讨论集中在对补丁的细节审查和小范围修正上，参与者们积极交流，确保补丁的质量和稳定性。

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

本邮件线程讨论了针对 ARM64 架构的嵌套虚拟化支持的补丁系列，主要由 Andre Przywara 和 Marc Zyngier 提出。

1. **原始补丁内容**：该补丁系列（v2）包含六个补丁，旨在为 ARM64 架构添加嵌套虚拟化支持。补丁包括更新内核头文件以支持新的 EL2 能力、引入新的命令行选项以启动 VCPU 在 EL2、以及设置维护 IRQ 的支持等。

2. **之前讨论要点**：虽然没有详细的历史讨论记录，但可以推测，之前的讨论可能集中在如何实现嵌套虚拟化的技术细节和潜在问题上。

3. **本周的新讨论与进展**：本周的讨论主要围绕补丁的具体实现和细节。Andre 提到补丁已在 FVP 和一些商业硬件上进行了测试，确保了嵌套虚拟化的功能。此外，Marc 对补丁中的 FEAT_E2H0 支持提出了一些建议，强调需要在用户空间中对不同选项进行清晰描述，并讨论了如何处理不支持 E2H0 的系统。整体上，参与者对补丁的功能和实现细节进行了深入的技术交流，确保了嵌套虚拟化的实现能够顺利进行。

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下允许用户空间写入 GICD_TYPER2.nASSGIcap 的补丁系列（PATCH v4 0/6）。该补丁旨在允许用户在初始化 VGIC（虚拟通用中断控制器）之前修改相关寄存器的值，以便更好地配置虚拟机的中断特性。

在历史讨论中，Oliver Upton 提出了多个补丁，主要包括对 VGIC ID 寄存器的写入权限进行调整，以及合并和简化对 VGICv3 维护中断的处理。Eric Auger 对这些补丁提出了一些建议和问题，主要集中在代码的可读性和逻辑一致性上。

在本周的新讨论中，Oliver 对 Eric 的反馈进行了回复，表示将根据建议更新补丁的变更日志，并确认了 GICD_IIDR 寄存器的设计意图。此外，关于文档中对用户空间控制主机分配的表述，Oliver 表达了希望去除该表述的意愿，认为这可能会给用户带来误解。

总体来看，讨论围绕着补丁的细节和文档的准确性展开，参与者积极交流以确保补丁的质量和清晰性。

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

本邮件线程讨论了针对 Armv8.8 SPE 特性的补丁集（[PATCH v5 00/12]），主要涉及三项新特性：FEAT_SPEv1p4 过滤器、FEAT_SPE_EFT 扩展过滤和 SPE_FEAT_FDS 数据源过滤。补丁的结构包括对系统寄存器的更改、各特性的支持以及相应的性能工具修改。

在历史讨论中，补丁经历了多个版本的迭代，主要改进包括修正了特性检测、优化了过滤器的实现方式，并增加了对新特性的文档说明。

本周的新讨论集中在补丁的具体实现上，James Clark 提交了12个补丁，涵盖了以下关键进展：
1. **系统寄存器更新**：新增 PMSFCR_EL1 和 PMSDSFR_EL1 字段，以支持 FEAT_SPE_EFT 和 FEAT_SPE_FDS。
2. **过滤器支持**：实现了 FEAT_SPEv1p4 和 FEAT_SPE_EFT 的过滤器，允许更灵活的事件选择。
3. **数据源过滤**：引入了对数据源的过滤支持，用户可以通过 inv_data_src_filter 来排除特定数据源。
4. **性能工具更新**：添加了对新配置字段 config4 的支持，以适应 SPE_FDS 的需求。

此外，文档也进行了更新，以详细说明新特性及其使用方法。整体来看，这些补丁为 Arm 架构的性能监控提供了更强大的功能和灵活性。

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

本邮件讨论的主题是关于对 ARMv8.8 SPE（Statistical Profiling Extension）特性的支持，特别是新增的三个特性：FEAT_SPEv1p4 过滤器、FEAT_SPE_EFT 扩展过滤和 SPE_FEAT_FDS 数据源过滤。

在历史讨论中，James Clark 提出了一个包含 12 个补丁的系列，旨在实现这些新特性。补丁的内容包括对系统寄存器的修改、性能监控工具的更新以及文档的补充。之前的讨论主要集中在如何实现这些特性以及与现有功能的兼容性。

本周的新讨论中，James Clark 提交了多个补丁，详细介绍了每个特性的实现细节。例如，FEAT_SPEv1p4 允许新增的过滤位，FEAT_SPE_EFT 则引入了用于现有加载、存储和分支过滤的掩码位。此外，SPE_FEAT_FDS 使得可以基于数据源 ID 进行过滤。补丁还增加了新的 `config4` 字段，以支持这些扩展功能，并更新了相关文档以反映这些变化。

总结来说，本周的进展主要是对新特性的实现和文档更新，确保这些新功能能够与现有的性能监控工具兼容并可用。

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

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 GICv3（通用中断控制器版本3）系统寄存器访问的修复和测试，包含四个补丁。

**原始补丁内容**：
Marc Zyngier 提出的补丁旨在解决一个用户空间无法访问 ICH_HCR_EL2 寄存器的问题。补丁包括修复系统寄存器表的排序、确保表格的排序检查，以及增加自测试以验证寄存器的可访问性。

**之前讨论要点**：
在历史讨论中，Marc 提出了四个补丁，分别是：
1. 修复 ICH_HCR_EL2 的排序问题。
2. 明确检查系统寄存器表的重置回调。
3. 强制 GICv3 系统寄存器表的排序。
4. 增加基本的 GICv3 系统寄存器用户空间访问测试。

**本周新讨论和进展**：
本周的讨论中，Itaru Kitayama 报告了在 RevC FVP 上测试自测的结果，并确认了测试的运行情况。Marc 对测试结果表示疑惑，并询问其来源。Sebastian Ott 对前三个补丁进行了审核并表示通过，确认了其有效性。整体来看，补丁的修复和测试工作得到了积极的反馈，推动了项目的进展。

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

本邮件线程讨论了一个关于KVM（Kernel-based Virtual Machine）在arm64架构下使用SMCCC 1.2进行FF-A（Firmware Framework for Arm）初始化的补丁（patch v7 2/5）。该补丁旨在确保在主机处理程序中正确处理FF-A调用。

在历史讨论中，参与者们探讨了FF-A规范中关于保留参数寄存器的使用，确认只需将这些寄存器置为零即可符合规范。Will Deacon和Per Larsen等人讨论了如何在EL2代理中处理不同的调用，并达成共识，认为应依赖EL3正确处理参数。

本周的新讨论中，Per Larsen指出，使用原始调用的功能ID在某些情况下可能导致错误，特别是在处理不同位宽的请求和响应时。他建议当前的v7补丁是最合适的选择。Will Deacon则提到，未检查源ID可能会导致安全问题，认为这是一个需要修复的bug。此外，讨论中还提到需要更新FF-A驱动以支持新规范中的64位FFA_RUN调用，以确保请求和响应能够正确处理。

总体来看，参与者们在补丁的有效性和安全性上达成了一定的共识，并计划进一步更新驱动以符合最新的规范。

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

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁系列，主要目标是允许用户空间写入 GICD_TYPER2.nASSGIcap 属性。

**原始补丁/问题内容**：
补丁系列的核心是允许用户空间在 VGIC（虚拟通用中断控制器）初始化之前修改 GICD_TYPER2.nASSGIcap，以便控制虚拟处理单元（vPE）的分配。这一功能在 GICv4.1 系统中尤为重要，因为它影响到虚拟中断的支持。

**之前讨论要点**：
在历史讨论中，补丁经历了多个版本的迭代，主要集中在修复一些细节问题，如中断请求的极性和对某些函数的调用进行了明确化。参与者们对补丁的实现细节进行了深入讨论，确保其在不同情况下的兼容性和稳定性。

**本周新讨论、进展或结论**：
本周的讨论中，补丁得到了进一步的完善和测试，包括对 nASSGIcap 属性的自测扩展，确保在 VGIC 初始化之前可以配置该属性，并验证在初始化后无法修改。参与者还讨论了如何将 vLPI 和 vSGI 的支持进行捆绑，以便用户空间可以控制 vPE 的分配。最终，补丁得到了相关人员的审核和认可，标志着该功能的实现即将完成。

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

本邮件线程讨论了两个补丁（patch），主要针对 ARM64 架构下的 KVM（Kernel-based Virtual Machine）系统寄存器和页面表的处理。

**原始补丁内容**：
第一个补丁（PATCH 1/2）提议在 `sys_regs` 中使用字符串选择助手，以简化代码结构。第二个补丁（PATCH 2/2）则建议在 `trace_handle_exit` 中同样使用字符串选择助手。

**之前讨论要点**：
在历史讨论中，Kuninori Morimoto 提出了这两个补丁，并得到了积极的反馈，表示将其应用到下一步开发中。

**本周新讨论进展**：
本周的讨论中，Oliver Upton 确认已将两个补丁应用到代码库中。此外，Raghavendra Rao Ananta 提出了两个新补丁，旨在改进大规模虚拟机的页面表销毁过程，以避免在销毁过程中出现的调度警告。具体而言，补丁将 `kvm_pgtable_stage2_destroy()` 函数拆分为两个部分，以便在处理较大页面表时能够定期调用 `cond_resched()`，从而减少 CPU 占用时间。Sean Christopherson 对补丁的描述提出了建议，认为应更明确地表达其功能。

总体来看，本周的讨论集中在补丁的应用和对页面表处理的优化上，显示出社区对性能和代码质量的持续关注。

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

本邮件讨论主题为“[PATCH 6.1.y] KVM: arm64: silence -Wuninitialized-const-pointer warning”，主要涉及在 Clang 22 中出现的一个警告，该警告指出传递给 `get_clidr_el1()` 的 `clidr` 变量是未初始化的常量指针。为了解决这个问题，Justin Stitt 提出了一个补丁，通过初始化 `clidr` 结构体来消除警告。该补丁仅适用于 6.1 版本，因为相关代码在后续版本中已被重构。

在本周的讨论中，参与者们对该补丁的有效性和必要性进行了深入探讨。Marc Zyngier 指出，该补丁并没有真正解决问题，只是掩盖了一个过于严格的警告，可能会导致设计上的不良后果。他建议应回溯应用一系列补丁，以改善代码质量。Greg KH 也对此表示质疑，认为不应为编译器的错误行为做出妥协，且 Clang 22 并不是 6.1.y 树的支持版本。

Nathan Chancellor 提到，虽然这个警告在构建日志中是唯一的稳定实例，但如果难以回溯补丁，可以考虑禁用该文件的警告，因为它是一个误报。讨论中还提到了一些关于常量指针的潜在未定义行为的问题。

总体来看，本周的讨论集中在补丁的合理性和代码质量的改善上，参与者们对如何处理编译器警告提出了不同的看法。

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

本邮件线程讨论了一个关于支持 Armv9.6 的新特性 FEAT_LSUI 的补丁集，该特性允许在内核中以不清除 PSTATE.PAN 位的方式访问用户内存。补丁集包含五个部分，主要涉及在 futex 原子操作中应用 FEAT_LSUI。

1. **原始补丁内容**：该补丁集的目标是支持 FEAT_LSUI，并在 futex 原子操作中进行应用。具体补丁包括添加 CPU 特性、将该特性暴露给虚拟机、更新 Kconfig、重构现有的 futex 原子操作实现，以及最终支持使用 FEAT_LSUI 的 futex 原子操作。

2. **之前讨论要点**：在补丁的历史版本中，开发者对补丁进行了多次重组和修改，主要集中在如何更好地暴露和实现 FEAT_LSUI 的功能，确保与现有代码的兼容性。

3. **本周新讨论与进展**：本周的讨论中，开发者 Yeoreum Yun 提交了补丁的最新版本，并对补丁的实现细节进行了说明。参与者 Marc Zyngier 提出建议，希望开发者在发布新版本时给予更多时间进行审查，以便提高代码质量。此外，Marc 还指出，考虑到即将到来的合并窗口，建议将该补丁集推迟到下一个版本进行进一步的打磨。

总的来说，本周的讨论主要集中在补丁的细节和审查流程上，开发者们对如何更好地实现和测试这一特性进行了深入交流。

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

本邮件线程讨论的主题是修复 ARM64 KVM 中的供应商 UUID 问题。Jack Thomson 提出的补丁旨在解决由于之前的提交（13423063c7cb）引入的字节序问题，导致生成的 UUID 与旧版本不匹配，从而影响与旧版客户机内核的兼容性，特别是影响了 PTP 设备的可用性。补丁通过更新宏的参数，使生成的 UUID 恢复到之前的值，以确保向后兼容。

在本周的讨论中，参与者们对此问题表示关注，并迅速达成共识。Marc Zyngier 和 Sudeep Holla 对补丁给予了认可，Marc 还提到他将帮助将补丁提交给 Linus。Will Deacon 也表示会处理此补丁，并感谢 Jack 的修复。Roman Kisel 对之前测试中未考虑旧内核的失误表示歉意，并承诺会进行必要的修正。

最终，补丁已被应用到 arm64 的修复分支中，确保了系统的稳定性和兼容性。

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 ARM64 架构下处理 SEA（Synchronous External Abort）的补丁（PATCH v2 1/6）。该补丁旨在实现虚拟机退出到用户空间，以更优雅地处理 SEA。

在历史讨论中，参与者主要集中在补丁的细节和实现方式上。Jiaqi Yan 和 Oliver Upton 讨论了如何避免在头文件中添加单一调用点的辅助函数，以及如何处理 FEAT_RAS（Fault Error Address Register）相关的内存访问错误。讨论中提到，即使故障代码指示为 TTW（Translation Table Walk），也需要区分是来自于客户机的阶段1 还是阶段2 的描述符物理地址。

在本周的新讨论中，Jiaqi Yan 提到他已经准备好 v3 版本的补丁，并希望确认最佳的提交选项。他指出，最近发现即使是新一代 ARM64 平台也需要依赖 KVM 来更好地处理 SEA，因为缺乏 APEI（ACPI Platform Error Interface）的支持。他强调希望尽快与上游合作，锁定提议的方法和用户空间接口（UAPI）。

总体而言，讨论围绕如何改进 KVM 对 SEA 的处理展开，参与者积极寻求最佳实践和合作机会。

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

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁系列，主要涉及 TCR2、SCTLR 和 MDCR 寄存器的配置驱动依赖性。

**原始补丁内容**：Marc Zyngier 提出了一个包含五个补丁的系列，旨在将 TCR2、SCTLR 和 MDCR 寄存器转换为配置驱动的清理框架。这些补丁主要是对之前 6.16 版本中遗留问题的修复，涉及对 TCR2_EL2、SCTLR_EL1 和 MDCR_EL2 的转换。

**之前讨论要点**：在历史讨论中，Oliver Upton 表示已经将这些补丁应用到下一个版本中，并提供了每个补丁的链接，确认了补丁的有效性。

**本周新讨论进展**：在本周的讨论中，Vlastimil Babka 报告了一个合并提交导致的 ./diff 文件问题，并指出这是由于本地残留文件造成的。Oliver Upton 随后表示已在下一个版本基础上添加了修复，并将纠正合并历史以便发送拉取请求。

总体来看，本周的讨论主要集中在修复合并问题上，确保补丁系列的顺利整合。

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

本邮件讨论的主题是关于为 KVM（Kernel-based Virtual Machine）在 arm64 架构下添加一个独立的自测试，用于检查 KVM 的 UUID。Marc Zyngier 提出了这个补丁，目的是为了在 UUID 出现问题时能够及时发现并报告。补丁中包含了新的测试文件 `kvm-uuid.c`，该文件实现了对 KVM UUID 的检查，并在 `Makefile.kvm` 中进行了相应的注册。

在之前的讨论中，Marc 提到 UUID 的处理非常复杂，容易出错，因此需要一个自测试来确保其正确性。Andrew Jones 提出了一个建议，认为在检查返回值时，应该确认 `res.a0` 是否等于 `SMCCC_RET_SUCCESS`，并建议引入一个通用的 `ucall` 辅助函数，以简化代码结构。

本周的新进展中，Sebastian Ott 对补丁进行了审核并表示支持。Andrew Jones 进一步讨论了自测试代码的现状，指出现有的 KVM 自测试代码大多是针对 x86 的，表示他不打算对此进行修改。

总体来看，本周讨论集中在补丁的细节和代码结构的优化上，参与者们对补丁的方向表示认可，并提出了一些建设性的建议。

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

本邮件线程讨论了一个关于 ARM64 架构的补丁，主题为“[PATCH v9 34/43] arm64: RME: Propagate number of breakpoints and watchpoints to userspace”。该补丁的目的是将断点和观察点的数量信息传递给用户空间，以便更好地支持调试和性能监控。

在历史讨论中并未提供具体的背景信息，因此我们无法得知该补丁的详细历史讨论内容。

在本周的新讨论中，参与者 Joey Gouly 对该补丁进行了审查，并给予了“Reviewed-by”的标记，表明他对补丁的认可和支持。此外，Joey Gouly 还对另一个补丁“[PATCH v9 36/43] arm64: RME: Initialize PMCR.N with number counter supported by RMM”进行了审查，同样给予了认可。这表明本周的讨论主要集中在对补丁的审查和确认上，显示出该补丁在社区中的接受度。

总体来看，本周的进展主要是对补丁的审查通过，为后续的合并奠定了基础。

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，主要内容是检查在访问 CPU 状态之前是否存在 SYSREGS_ON_CPU 的条件。

在历史讨论中，Marc Zyngier 提出了一个补丁，旨在解决由于未检查系统寄存器是否已加载而导致的外部中止自测失败的问题。该问题源于 VHE（Virtualization Host Extensions）环境下，相关代码在异常发生时未能正确处理寄存器的可见性，导致潜在的严重错误。因此，补丁增加了必要的检查，并强调了这一检查的重要性。

在本周的新讨论中，Oliver Upton 回复表示已将该补丁应用到下一步的开发中，确认了补丁的有效性和必要性。这标志着该问题的解决方案得到了认可，并将继续推进。

总结而言，该补丁旨在修复 KVM 在 arm64 环境下的一个关键问题，历史讨论中明确了问题的严重性，而本周的进展则是补丁的成功应用。

#### 📝 邮件列表

1. **[07-20 11:22]** [PATCH] KVM: arm64: Check for SYSREGS_ON_CPU before accessing the CPU state
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-21 15:24]** Re: [PATCH] KVM: arm64: Check for SYSREGS_ON_CPU before accessing the CPU state
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 21: [PATCH v4 01/23] arm64: cpufeature: Add cpucap for HPMN0

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 21 Jul 2025 18:00:34 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构的补丁（patch），标题为“[PATCH v4 01/23] arm64: cpufeature: Add cpucap for HPMN0”。该补丁的目的是为 ARM64 处理器的特性添加一个新的 CPU 能力标志（cpucap），具体是 HPMN0。

在历史讨论部分，由于没有提供相关内容，因此无法总结之前的讨论要点。

在本周的新讨论中，参与者 Colton Lewis 对补丁进行了回复，感谢了 Suzuki K Poulose 的审查意见，并表示将根据反馈进行相应的修改。这表明补丁正在接受审查，并且开发者愿意根据反馈进行调整，以确保其适用性和正确性。

总体来看，本周的讨论主要集中在补丁的审查和修改上，尚未有进一步的技术细节或进展更新。

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）中嵌套虚拟化自测试的补丁（RFC PATCH v2 0/9）。该补丁旨在启用嵌套虚拟化的自测试功能，但在实施过程中引发了一些争议。

在历史讨论中，Marc Zyngier 提出了对补丁的看法，询问是否认为这些补丁在不支持裸金属虚拟机的情况下仍然有价值，或者是否需要重新修改以支持递归虚拟机。

本周的新讨论中，Ganapatrao Kulkarni 对补丁的实现方式提出了批评。他认为，现有的测试应聚焦于在 EL2（异常级别2）下的运行，而不是嵌套虚拟化的概念。他建议在补丁中去掉与嵌套相关的内容，专注于 EL2 的两种实现方式。此外，他强调 EL2 测试不应是可选的，应该在 EL2 可用时自动运行，而不需要额外选项。他对补丁的进展表示担忧，认为在他提出这些要求后，几个月内没有实质性进展。

总结来看，当前讨论集中在补丁的实现细节及其必要性上，参与者对如何有效地进行嵌套虚拟化自测试有不同的看法。

#### 📝 邮件列表

1. **[07-25 15:31]** Re: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
2. **[07-25 11:59]** Re: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [RFC PATCH 2/2] KVM: arm64: vgic-its: Unmap all vPEs on shutdown

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 22 Jul 2025 15:46:29 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主题为“在关机时解除所有虚拟处理单元（vPEs）的映射”。该补丁旨在确保在系统关闭时，所有虚拟处理单元能够正确解除与中断控制器的映射，以避免潜在的状态问题。

在历史讨论中，参与者提到需要在解除映射之前将 vPEs 从重分发器中设置为非驻留状态，以防止消耗未知的 vPE 状态。此外，讨论中提到在关机过程中，可能需要在 `kvm_arch_disable_virtualization_cpu()` 函数中对 vPE 进行去调度处理。

本周的新讨论中，Oliver Upton 和 David Woodhouse 进一步探讨了补丁的实现细节。Oliver 指出，当前的实现假设 vCPUs 已经被静默处理，并讨论了在未来希望实现的 kexec 功能，即在某些物理 CPU 仍在运行虚拟 CPU 的情况下进行 kexec。David 也提到，当前的 GIC（通用中断控制器）在静默时并未停止访问内存，这导致了一些性能问题。此外，他们还讨论了 GIC 的 DMA 散射问题对 KVM 主机和客人系统的影响，尤其是在系统休眠和恢复时可能导致的内存损坏。

总体而言，讨论集中在确保在关机时正确处理虚拟处理单元的映射，以及未来可能的改进方向。

#### 📝 邮件列表

1. **[07-22 15:46]** Re: [RFC PATCH 2/2] KVM: arm64: vgic-its: Unmap all vPEs on shutdown
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-23 11:42]** Re: [RFC PATCH 2/2] KVM: arm64: vgic-its: Unmap all vPEs on shutdown
   - 发件人: David Woodhouse <dwmw2@infradead.org>

---

### Thread 3: [RFC PATCH 2/2] KVM: arm64: vgic-its: Unmap all vPEs on shutdown

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Jul 2025 12:35:40 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下的 vgic-its（虚拟通用中断控制器）的一个补丁，具体内容为在系统关闭时解除所有虚拟处理单元（vPEs）的映射。该补丁的目的是确保在关闭操作时，所有 vPEs 被正确解除映射，以避免潜在的资源泄漏或中断处理问题。

在之前的讨论中，虽然没有具体的邮件记录，但可以推测出参与者对如何在系统关闭时正确处理 GIC（通用中断控制器）存在疑问，尤其是操作系统应如何安静地处理 GIC 的状态。

在本周的新讨论中，参与者 David Woodhouse 对该补丁表示关注，并请求来自 Arm 的指导，以明确操作系统在此过程中应遵循的预期行为。这表明该补丁仍在寻求社区的反馈和建议，以确保其实现的合理性和有效性。

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

在本次邮件讨论中，主要关注的是与提交 efa1368ba9f4 相关的 KVM（Kernel-based Virtual Machine）外部中断（external_aborts）测试失败的问题。Jiaqi Yan 在进行 SEA（Synchronous Exception Acknowledgment）注入开发时，发现位于 tools/testing/selftests/kvm/arm64/external_aborts.c 的测试在其本地跟踪的 kvmarm/next 版本中失败，具体表现为寄存器中的程序计数器（PC）值不符合预期。

Jiaqi 提到，回退提交 efa1368ba9f4 后，所有相关测试均通过，暗示该提交可能引入了某个 bug。尽管他尚未确定具体问题，但认为可能与 KVM 向客户机注入 SEA 的代码有关。

在本周的讨论中，Jiaqi 进行了友好的提醒，期望得到进一步的反馈。Marc Zyngier 也参与了讨论，并提供了一个相关的提交链接，暗示可能与此问题相关的代码变更。整体来看，讨论集中在确认和解决由 efa1368ba9f4 提交引发的外部中断测试失败的问题上。

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

本邮件讨论的主题是关于 KVM 在 arm64 架构下的一个 bug 报告，具体涉及在使用透明大页（transparent huge pages）时，启动 pkvm 客户机导致的内核崩溃问题。崩溃信息显示在 `arch/arm64/kvm/hyp/nvhe/mem_protect.c` 文件的第 1088 行。

在本周的讨论中，参与者 Ben Horgan 提出了一个补丁，旨在解决该崩溃问题。补丁的核心内容是修改 `__pkvm_host_relax_perms_guest()` 函数中的 `assert_host_shared_guest()` 调用，将其从固定的页面大小参数改为动态获取，从而避免了在处理块映射时的错误假设。Ben 表示，应用该补丁后，崩溃问题得以解决。

总结来说，本周的讨论集中在一个特定的 bug 修复上，Ben 提出的补丁有效地解决了在使用透明大页时启动 pkvm 客户机导致的内核崩溃问题，显示了对 KVM arm64 代码的深入分析与修正。

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

本邮件线程讨论了 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 vgic-its（虚拟通用中断控制器）相关问题，具体是关于返回 -ENXIO 错误码以处理无效的 KVM_DEV_ARM_VGIC_GRP_CTRL 属性。

在历史讨论中，虽然没有具体的邮件记录，但可以推测这是一个针对 KVM 设备控制属性的修复或改进提案，旨在提高错误处理的准确性和系统稳定性。

本周的新讨论中，David Woodhouse 提出了对该补丁的跟进，询问进展情况。随后，Oliver Upton 回复确认该补丁已被应用到下一个版本中，并提供了补丁的链接。这表明该补丁得到了认可并将继续推进，反映出社区对该问题的重视和快速响应。

总结而言，本周的讨论主要集中在确认补丁的应用上，标志着对 KVM 中断控制器属性处理的改进即将生效。

#### 📝 邮件列表

1. **[07-22 12:33]** Re: KVM: arm64: vgic-its: Return -ENXIO to invalid
 KVM_DEV_ARM_VGIC_GRP_CTRL attrs
   - 发件人: David Woodhouse <dwmw2@infradead.org>
2. **[07-23 23:49]** Re: KVM: arm64: vgic-its: Return -ENXIO to invalid KVM_DEV_ARM_VGIC_GRP_CTRL attrs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

