# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 10:23:08

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 327
- **总 Thread 数**: 31
- **大型 Thread** (>20封): 3 个

### 分类分布

- **PATCH**: 25 threads (198 邮件)
- **RFC**: 2 threads (116 邮件)
- **Bug Report**: 2 threads (6 邮件)
- **Selftest**: 1 threads (3 邮件)
- **GIT PULL**: 1 threads (4 邮件)

---

## 📌 PATCH

共 25 个 thread

---

### Thread 1: [PATCH v17 00/24] KVM: Enable mmap() for guest_memfd

**📧 邮件数**: 48 | **👥 参与者**: 5 | **📅 开始时间**: Tue, 29 Jul 2025 15:54:31 -0700

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）中支持 mmap() 操作的 guest_memfd 的补丁（PATCH v17 00/24）。该补丁的主要目的是为不使用 KVM_MEMORY_ATTRIBUTE_PRIVATE 的虚拟机类型提供对 guest_memfd 支持的 mmap() 功能。

历史讨论中，补丁的背景是为了增强 KVM 的内存管理能力，特别是在处理机密虚拟机和非机密虚拟机时提供统一的内存管理模型。补丁的实施将允许 VMM（虚拟机监控程序）如 Firecracker 完全基于 guest_memfd 运行虚拟机，并增强安全性，减少主机内核对虚拟机内存的直接映射。

在本周的新讨论中，参与者们确认了补丁的各个部分，并进行了多项修订和测试。补丁的关键更新包括：
1. 为 x86 和 arm64 架构启用 guest_memfd 的 mmap() 支持。
2. 引入新的内存标志 KVM_MEMSLOT_GMEM_ONLY，以优化内存槽的管理。
3. 更新自测用例，确保在支持 mmap() 的情况下，guest_memfd 的功能正常。

总体而言，补丁的实施和讨论进展顺利，参与者们对补丁的各个方面表示认可，并进行了必要的代码审查和测试。

#### 📝 邮件列表

1. **[07-29 15:54]** [PATCH v17 00/24] KVM: Enable mmap() for guest_memfd
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[07-29 15:54]** [PATCH v17 01/24] KVM: Rename CONFIG_KVM_PRIVATE_MEM to CONFIG_KVM_GUEST_MEMFD
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[07-29 15:54]** [PATCH v17 02/24] KVM: x86: Have all vendor neutral sub-configs
 depend on KVM_X86, not just KVM
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[07-29 15:54]** [PATCH v17 03/24] KVM: x86: Select KVM_GENERIC_PRIVATE_MEM directly
 from KVM_SW_PROTECTED_VM
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[07-29 15:54]** [PATCH v17 04/24] KVM: x86: Select TDX's KVM_GENERIC_xxx dependencies
 iff CONFIG_KVM_INTEL_TDX=y
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[07-29 15:54]** [PATCH v17 05/24] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_HAVE_KVM_ARCH_GMEM_POPULATE
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[07-29 15:54]** [PATCH v17 06/24] KVM: Rename kvm_slot_can_be_private() to kvm_slot_has_gmem()
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[07-29 15:54]** [PATCH v17 07/24] KVM: Fix comments that refer to slots_lock
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[07-29 15:54]** [PATCH v17 08/24] KVM: Fix comment that refers to kvm uapi header path
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[07-29 15:54]** [PATCH v17 09/24] KVM: x86: Enable KVM_GUEST_MEMFD for all 64-bit builds
   - 发件人: Sean Christopherson <seanjc@google.com>
11. **[07-29 15:54]** [PATCH v17 10/24] KVM: guest_memfd: Add plumbing to host to map
 guest_memfd pages
   - 发件人: Sean Christopherson <seanjc@google.com>
12. **[07-29 15:54]** [PATCH v17 11/24] KVM: guest_memfd: Track guest_memfd mmap support in memslot
   - 发件人: Sean Christopherson <seanjc@google.com>
13. **[07-29 15:54]** [PATCH v17 12/24] KVM: x86/mmu: Rename .private_max_mapping_level()
 to .gmem_max_mapping_level()
   - 发件人: Sean Christopherson <seanjc@google.com>
14. **[07-29 15:54]** [PATCH v17 13/24] KVM: x86/mmu: Hoist guest_memfd max level/order
 helpers "up" in mmu.c
   - 发件人: Sean Christopherson <seanjc@google.com>
15. **[07-29 15:54]** [PATCH v17 14/24] KVM: x86/mmu: Enforce guest_memfd's max order when
 recovering hugepages
   - 发件人: Sean Christopherson <seanjc@google.com>
16. **[07-29 15:54]** [PATCH v17 15/24] KVM: x86/mmu: Extend guest_memfd's max mapping
 level to shared mappings
   - 发件人: Sean Christopherson <seanjc@google.com>
17. **[07-29 15:54]** [PATCH v17 16/24] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Sean Christopherson <seanjc@google.com>
18. **[07-29 15:54]** [PATCH v17 17/24] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Sean Christopherson <seanjc@google.com>
19. **[07-29 15:54]** [PATCH v17 18/24] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Sean Christopherson <seanjc@google.com>
20. **[07-29 15:54]** [PATCH v17 19/24] KVM: arm64: nv: Handle VNCR_EL2-triggered faults
 backed by guest_memfd
   - 发件人: Sean Christopherson <seanjc@google.com>
21. **[07-29 15:54]** [PATCH v17 20/24] KVM: arm64: Enable support for guest_memfd backed memory
   - 发件人: Sean Christopherson <seanjc@google.com>
22. **[07-29 15:54]** [PATCH v17 21/24] KVM: Allow and advertise support for host mmap() on
 guest_memfd files
   - 发件人: Sean Christopherson <seanjc@google.com>
23. **[07-29 15:54]** [PATCH v17 22/24] KVM: selftests: Do not use hardcoded page sizes in
 guest_memfd test
   - 发件人: Sean Christopherson <seanjc@google.com>
24. **[07-29 15:54]** [PATCH v17 23/24] KVM: selftests: guest_memfd mmap() test when mmap
 is supported
   - 发件人: Sean Christopherson <seanjc@google.com>
25. **[07-29 15:54]** [PATCH v17 24/24] KVM: selftests: Add guest_memfd testcase to
 fault-in on !mmap()'d memory
   - 发件人: Sean Christopherson <seanjc@google.com>
26. **[07-30 15:33]** Re: [PATCH v17 14/24] KVM: x86/mmu: Enforce guest_memfd's max order
 when recovering hugepages
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
27. **[07-30 15:36]** Re: [PATCH v17 15/24] KVM: x86/mmu: Extend guest_memfd's max mapping
 level to shared mappings
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
28. **[07-30 15:37]** Re: [PATCH v17 16/24] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
29. **[07-30 16:20]** Re: [PATCH v17 24/24] KVM: selftests: Add guest_memfd testcase to
 fault-in on !mmap()'d memory
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
30. **[07-30 19:04]** Re: [PATCH v17 22/24] KVM: selftests: Do not use hardcoded page sizes
 in guest_memfd test
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
31. **[07-30 19:39]** Re: [PATCH v17 23/24] KVM: selftests: guest_memfd mmap() test when
 mmap is supported
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
32. **[07-30 05:57]** Re: [PATCH v17 23/24] KVM: selftests: guest_memfd mmap() test when
 mmap is supported
   - 发件人: Sean Christopherson <seanjc@google.com>
33. **[07-30 16:51]** Re: [PATCH v17 24/24] KVM: selftests: Add guest_memfd testcase to
 fault-in on !mmap()'d memory
   - 发件人: Fuad Tabba <tabba@google.com>
34. **[07-30 14:34]** Re: [PATCH v17 00/24] KVM: Enable mmap() for guest_memfd
   - 发件人: Ackerley Tng <ackerleytng@google.com>
35. **[07-30 15:44]** Re: [PATCH v17 00/24] KVM: Enable mmap() for guest_memfd
   - 发件人: Ackerley Tng <ackerleytng@google.com>
36. **[07-31 15:49]** Re: [PATCH v17 23/24] KVM: selftests: guest_memfd mmap() test when
 mmap is supported
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
37. **[07-31 09:59]** Re: [PATCH v17 13/24] KVM: x86/mmu: Hoist guest_memfd max level/order
 helpers "up" in mmu.c
   - 发件人: David Hildenbrand <david@redhat.com>
38. **[07-31 10:01]** Re: [PATCH v17 15/24] KVM: x86/mmu: Extend guest_memfd's max mapping
 level to shared mappings
   - 发件人: David Hildenbrand <david@redhat.com>
39. **[07-31 09:05]** Re: [PATCH v17 15/24] KVM: x86/mmu: Extend guest_memfd's max mapping
 level to shared mappings
   - 发件人: Fuad Tabba <tabba@google.com>
40. **[07-31 09:06]** Re: [PATCH v17 13/24] KVM: x86/mmu: Hoist guest_memfd max level/order
 helpers "up" in mmu.c
   - 发件人: Fuad Tabba <tabba@google.com>
41. **[07-31 10:06]** Re: [PATCH v17 14/24] KVM: x86/mmu: Enforce guest_memfd's max order
 when recovering hugepages
   - 发件人: David Hildenbrand <david@redhat.com>
42. **[07-31 09:07]** Re: [PATCH v17 04/24] KVM: x86: Select TDX's KVM_GENERIC_xxx
 dependencies iff CONFIG_KVM_INTEL_TDX=y
   - 发件人: Fuad Tabba <tabba@google.com>
43. **[07-31 09:08]** Re: [PATCH v17 03/24] KVM: x86: Select KVM_GENERIC_PRIVATE_MEM
 directly from KVM_SW_PROTECTED_VM
   - 发件人: Fuad Tabba <tabba@google.com>
44. **[07-31 09:08]** Re: [PATCH v17 02/24] KVM: x86: Have all vendor neutral sub-configs
 depend on KVM_X86, not just KVM
   - 发件人: Fuad Tabba <tabba@google.com>
45. **[07-31 09:10]** Re: [PATCH v17 14/24] KVM: x86/mmu: Enforce guest_memfd's max order
 when recovering hugepages
   - 发件人: Fuad Tabba <tabba@google.com>
46. **[07-31 09:15]** Re: [PATCH v17 12/24] KVM: x86/mmu: Rename .private_max_mapping_level()
 to .gmem_max_mapping_level()
   - 发件人: Fuad Tabba <tabba@google.com>
47. **[07-31 10:29]** Re: [PATCH v17 12/24] KVM: x86/mmu: Rename
 .private_max_mapping_level() to .gmem_max_mapping_level()
   - 发件人: David Hildenbrand <david@redhat.com>
48. **[07-31 09:33]** Re: [PATCH v17 12/24] KVM: x86/mmu: Rename .private_max_mapping_level()
 to .gmem_max_mapping_level()
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 2: [PATCH v3 00/29] KVM: arm64: SMMUv3 driver for pKVM

**📧 邮件数**: 39 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 28 Jul 2025 17:52:47 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 的 ARM SMMUv3 驱动的多个补丁，主要集中在为 pKVM 提供 DMA 隔离支持的实现。以下是讨论的主要内容：

1. **原始补丁内容**：补丁系列的核心是为 pKVM 提供 SMMUv3 驱动，支持 DMA 隔离。该补丁将 SMMUv3 驱动集成到 KVM 中，以确保主机无法访问来宾或虚拟机的内存。

2. **历史讨论要点**：之前的讨论主要集中在如何实现 SMMUv3 驱动的结构，包括如何处理 DMA 隔离、如何在 hypervisor 和主机之间共享资源等。补丁中提到的设计包括将 SMMU 表和命令队列映射到 hypervisor 地址空间，并在初始化过程中处理相关的硬件寄存器。

3. **本周的新讨论与进展**：本周的讨论中，补丁逐步完善，增加了 IOMMU 操作的实现，支持设备的启用和禁用功能。讨论中还提到需要将 SMMUv3 驱动分为主机和 hypervisor 部分，以便在 pKVM 模式下有效管理设备。补丁还引入了命令队列的设置和流表的管理，确保在 hypervisor 中能够正确处理设备请求。

此外，参与者对补丁的结构和命名提出了建议，强调需要清晰地区分 pKVM 和常规 IOMMU 驱动的功能，以避免混淆。整体来看，这一系列补丁旨在增强 KVM 在保护模式下的设备隔离和管理能力。

#### 📝 邮件列表

1. **[07-28 17:52]** [PATCH v3 00/29] KVM: arm64: SMMUv3 driver for pKVM
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[07-28 17:52]** [PATCH v3 01/29] KVM: arm64: Add a new function to donate memory with prot
   - 发件人: Mostafa Saleh <smostafa@google.com>
3. **[07-28 17:52]** [PATCH v3 02/29] KVM: arm64: Donate MMIO to the hypervisor
   - 发件人: Mostafa Saleh <smostafa@google.com>
4. **[07-28 17:52]** [PATCH v3 03/29] KVM: arm64: pkvm: Add pkvm_time_get()
   - 发件人: Mostafa Saleh <smostafa@google.com>
5. **[07-28 17:52]** [PATCH v3 04/29] iommu/io-pgtable-arm: Split the page table driver
   - 发件人: Mostafa Saleh <smostafa@google.com>
6. **[07-28 17:52]** [PATCH v3 05/29] iommu/io-pgtable-arm: Split initialization
   - 发件人: Mostafa Saleh <smostafa@google.com>
7. **[07-28 17:52]** [PATCH v3 06/29] iommu/arm-smmu-v3: Move some definitions to a new
 common file
   - 发件人: Mostafa Saleh <smostafa@google.com>
8. **[07-28 17:52]** [PATCH v3 07/29] iommu/arm-smmu-v3: Extract driver-specific bits from
 probe function
   - 发件人: Mostafa Saleh <smostafa@google.com>
9. **[07-28 17:52]** [PATCH v3 08/29] iommu/arm-smmu-v3: Move some functions to arm-smmu-v3-common.c
   - 发件人: Mostafa Saleh <smostafa@google.com>
10. **[07-28 17:52]** [PATCH v3 09/29] iommu/arm-smmu-v3: Move queue and table allocation
 to arm-smmu-v3-common.c
   - 发件人: Mostafa Saleh <smostafa@google.com>
11. **[07-28 17:52]** [PATCH v3 10/29] iommu/arm-smmu-v3: Move firmware probe to arm-smmu-v3-common
   - 发件人: Mostafa Saleh <smostafa@google.com>
12. **[07-28 17:52]** [PATCH v3 11/29] iommu/arm-smmu-v3: Move IOMMU registration to arm-smmu-v3-common.c
   - 发件人: Mostafa Saleh <smostafa@google.com>
13. **[07-28 17:52]** [PATCH v3 12/29] iommu/arm-smmu-v3: Split cmdq code with hyp
   - 发件人: Mostafa Saleh <smostafa@google.com>
14. **[07-28 17:53]** [PATCH v3 13/29] iommu/arm-smmu-v3: Move TLB range invalidation into
 a macro
   - 发件人: Mostafa Saleh <smostafa@google.com>
15. **[07-28 17:53]** [PATCH v3 14/29] KVM: arm64: iommu: Introduce IOMMU driver infrastructure
   - 发件人: Mostafa Saleh <smostafa@google.com>
16. **[07-28 17:53]** [PATCH v3 15/29] KVM: arm64: iommu: Shadow host stage-2 page table
   - 发件人: Mostafa Saleh <smostafa@google.com>
17. **[07-28 17:53]** [PATCH v3 16/29] KVM: arm64: iommu: Add a memory pool
   - 发件人: Mostafa Saleh <smostafa@google.com>
18. **[07-28 17:53]** [PATCH v3 17/29] KVM: arm64: iommu: Add enable/disable hypercalls
   - 发件人: Mostafa Saleh <smostafa@google.com>
19. **[07-28 17:53]** [PATCH v3 18/29] iommu/arm-smmu-v3-kvm: Add SMMUv3 driver
   - 发件人: Mostafa Saleh <smostafa@google.com>
20. **[07-28 17:53]** [PATCH v3 19/29] iommu/arm-smmu-v3-kvm: Initialize registers
   - 发件人: Mostafa Saleh <smostafa@google.com>
21. **[07-28 17:53]** [PATCH v3 20/29] iommu/arm-smmu-v3-kvm: Setup command queue
   - 发件人: Mostafa Saleh <smostafa@google.com>
22. **[07-28 17:53]** [PATCH v3 21/29] iommu/arm-smmu-v3-kvm: Setup stream table
   - 发件人: Mostafa Saleh <smostafa@google.com>
23. **[07-28 17:53]** [PATCH v3 22/29] iommu/arm-smmu-v3-kvm: Reset the device
   - 发件人: Mostafa Saleh <smostafa@google.com>
24. **[07-28 17:53]** [PATCH v3 23/29] iommu/arm-smmu-v3-kvm: Support io-pgtable
   - 发件人: Mostafa Saleh <smostafa@google.com>
25. **[07-28 17:53]** [PATCH v3 24/29] iommu/arm-smmu-v3-kvm: Shadow the CPU stage-2 page table
   - 发件人: Mostafa Saleh <smostafa@google.com>
26. **[07-28 17:53]** [PATCH v3 25/29] iommu/arm-smmu-v3-kvm: Add enable/disable device HVCs
   - 发件人: Mostafa Saleh <smostafa@google.com>
27. **[07-28 17:53]** [PATCH v3 26/29] iommu/arm-smmu-v3-kvm: Add host driver for pKVM
   - 发件人: Mostafa Saleh <smostafa@google.com>
28. **[07-28 17:53]** [PATCH v3 27/29] iommu/arm-smmu-v3-kvm: Pass a list of SMMU devices
 to the hypervisor
   - 发件人: Mostafa Saleh <smostafa@google.com>
29. **[07-28 17:53]** [PATCH v3 28/29] iommu/arm-smmu-v3-kvm: Allocate structures and reset device
   - 发件人: Mostafa Saleh <smostafa@google.com>
30. **[07-28 17:53]** [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Mostafa Saleh <smostafa@google.com>
31. **[07-29 08:44]** Re: [PATCH v3 20/29] iommu/arm-smmu-v3-kvm: Setup command queue
   - 发件人: Krzysztof Kozlowski <krzk@kernel.org>
32. **[07-29 09:55]** Re: [PATCH v3 20/29] iommu/arm-smmu-v3-kvm: Setup command queue
   - 发件人: Mostafa Saleh <smostafa@google.com>
33. **[07-30 11:42]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
34. **[07-30 15:07]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Mostafa Saleh <smostafa@google.com>
35. **[07-30 13:47]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
36. **[07-31 14:17]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Mostafa Saleh <smostafa@google.com>
37. **[07-31 13:57]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
38. **[07-31 17:44]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Mostafa Saleh <smostafa@google.com>
39. **[08-01 15:59]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>

---

### Thread 3: [PATCH 0/5] KVM: Drop vm_dead, pivot on vm_bugged for -EIO

**📧 邮件数**: 20 | **👥 参与者**: 6 | **📅 开始时间**: Tue, 29 Jul 2025 12:33:35 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 的补丁系列，主题为「KVM: Drop vm_dead, pivot on vm_bugged for -EIO」。该补丁的主要目的是去除 `vm_dead` 标志，改为仅基于 `vm_bugged` 来拒绝 ioctl 调用，以提高系统的安全性和稳定性。

在历史讨论中，补丁的提出者 Sean Christopherson 指出，`vm_dead` 的检查存在竞争条件，可能导致错误的安全感。之前的讨论集中在如何处理虚拟机的状态，尤其是在遇到内核或硬件错误时，如何有效地限制对虚拟机的操作。

本周的新讨论中，Sean 提出了五个补丁，具体包括：
1. **补丁 1**：确保 `KVM_REQ_VM_DEAD` 不会被清除，以防止虚拟机重新进入客体。
2. **补丁 2**：在遇到意外的 S-EPT 违规时，退出用户空间并返回 `-EFAULT`，而不是将虚拟机标记为死亡。
3. **补丁 3**：仅在虚拟机出现错误时拒绝 ioctl 调用，允许在虚拟机被明确终止的情况下进行 ioctl 操作。
4. **补丁 4**：改进自测代码，以处理所有成功的 SEV 迁移。
5. **补丁 5**：添加子 ioctl `KVM_TDX_TERMINATE_VM`，以在关闭前释放 HKID，从而提高私有内存的回收效率。

讨论中还涉及了对补丁的审查和建议，参与者们对补丁的有效性和潜在问题进行了深入探讨，特别是如何确保在虚拟机状态变更时的安全性。整体来看，这些补丁旨在增强 KVM 的稳定性和安全性，减少因错误状态引发的问题。

#### 📝 邮件列表

1. **[07-29 12:33]** [PATCH 0/5] KVM: Drop vm_dead, pivot on vm_bugged for -EIO
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[07-29 12:33]** [PATCH 1/5] KVM: Never clear KVM_REQ_VM_DEAD from a vCPU's requests
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[07-29 12:33]** [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected pending
 S-EPT Violation
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[07-29 12:33]** [PATCH 3/5] KVM: Reject ioctls only if the VM is bugged, not simply
 marked dead
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[07-29 12:33]** [PATCH 4/5] KVM: selftests: Use for-loop to handle all successful SEV migrations
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[07-29 12:33]** [PATCH 5/5] KVM: TDX: Add sub-ioctl KVM_TDX_TERMINATE_VM
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[07-29 22:27]** Re: [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected
 pending S-EPT Violation
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
8. **[07-29 15:54]** Re: [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected
 pending S-EPT Violation
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[07-29 22:58]** Re: [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected
 pending S-EPT Violation
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
10. **[07-29 16:08]** Re: [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected
 pending S-EPT Violation
   - 发件人: Sean Christopherson <seanjc@google.com>
11. **[07-29 23:13]** Re: [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected
 pending S-EPT Violation
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
12. **[07-30 09:20]** Re: [PATCH 3/5] KVM: Reject ioctls only if the VM is bugged, not
 simply marked dead
   - 发件人: Chao Gao <chao.gao@intel.com>
13. **[07-30 10:07]** Re: [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected
 pending S-EPT Violation
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
14. **[07-30 13:45]** Re: [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected
 pending S-EPT Violation
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
15. **[07-30 13:55]** Re: [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected
 pending S-EPT Violation
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
16. **[07-30 14:04]** Re: [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected
 pending S-EPT Violation
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
17. **[07-30 12:59]** Re: [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected
 pending S-EPT Violation
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
18. **[08-01 16:56]** Re: [PATCH 5/5] KVM: TDX: Add sub-ioctl KVM_TDX_TERMINATE_VM
   - 发件人: Adrian Hunter <adrian.hunter@intel.com>
19. **[08-01 09:44]** Re: [PATCH 5/5] KVM: TDX: Add sub-ioctl KVM_TDX_TERMINATE_VM
   - 发件人: Sean Christopherson <seanjc@google.com>
20. **[08-03 20:41]** Re: [PATCH 5/5] KVM: TDX: Add sub-ioctl KVM_TDX_TERMINATE_VM
   - 发件人: Adrian Hunter <adrian.hunter@intel.com>

---

### Thread 4: [PATCH v1 0/8] KVM: arm64: Reserve pKVM VM handle during initial VM setup

**📧 邮件数**: 10 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 29 Jul 2025 13:00:05 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁系列，主要目的是在初始虚拟机（VM）设置过程中保留 pKVM VM 句柄。该补丁系列分为八个部分，主要涉及重命名、重构和修复现有问题，以便在主机初始化 VM 时提前创建句柄。

在历史讨论中，补丁的背景是 pKVM 中的句柄在虚拟机初始化时分配，但主机在此之前就开始初始化 VM，这导致 MMU 通知依赖于尚未创建的句柄。为了解决这个问题，补丁提议将句柄的创建移动到主机初始化 VM 时。

本周的新讨论中，Fuad Tabba 提出了多个补丁，包括：
1. 重命名和澄清代码中的字段和注释，以提高可读性。
2. 将句柄的创建与虚拟机的初始化状态解耦，增加了新的布尔标志以跟踪虚拟机是否已创建。
3. 引入新的超调用接口，允许主机在虚拟机的生命周期中更灵活地管理句柄的保留和初始化。
4. 最后一个补丁确保在主机 VM 初始化时保留 pKVM 句柄，以避免在 MMU 通知触发时句柄尚未创建的情况。

总的来说，本周的讨论集中在补丁的具体实现和代码的清晰度上，确保在未来的开发中能够更好地管理 pKVM 的虚拟机句柄。

#### 📝 邮件列表

1. **[07-29 13:00]** [PATCH v1 0/8] KVM: arm64: Reserve pKVM VM handle during initial VM setup
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[07-29 13:00]** [PATCH v1 1/8] KVM: arm64: Rename pkvm.enabled to pkvm.is_protected
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[07-29 13:00]** [PATCH v1 2/8] KVM: arm64: Rename 'host_kvm' to 'kvm' in pKVM host code
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[07-29 13:00]** [PATCH v1 3/8] KVM: arm64: Clarify comments to distinguish pKVM mode
 from protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[07-29 13:00]** [PATCH v1 4/8] KVM: arm64: Decouple hyp VM creation state from its handle
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[07-29 13:00]** [PATCH v1 5/8] KVM: arm64: Separate allocation and insertion of pKVM
 VM table entries
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[07-29 13:00]** [PATCH v1 6/8] KVM: arm64: Consolidate pKVM hypervisor VM
 initialization logic
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[07-29 13:00]** [PATCH v1 7/8] KVM: arm64: Introduce separate hypercalls for pKVM VM
 reservation and initialization
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[07-29 13:00]** [PATCH v1 8/8] KVM: arm64: Reserve pKVM handle during pkvm_init_host_vm()
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[08-03 14:10]** Re: [PATCH v1 1/8] KVM: arm64: Rename pkvm.enabled to
 pkvm.is_protected
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>

---

### Thread 5: [PATCH 0/2] Dump instructions on panic for pKVM/nvhe

**📧 邮件数**: 10 | **👥 参与者**: 4 | **📅 开始时间**: Thu, 17 Jul 2025 23:47:42 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是针对 pKVM/nvhe 的内核补丁，主要目的是在系统发生 panic 时能够转储故障指令。历史讨论中，Mostafa Saleh 提出了两个补丁：第一个补丁（PATCH 1/2）实现了在 nvhe 模式下的 panic 时打印指令代码，第二个补丁（PATCH 2/2）则计划为 pKVM 添加类似功能。历史讨论中，参与者对补丁的实现细节进行了讨论，特别是如何处理不同配置下的堆栈跟踪。

在本周的新讨论中，Oliver Upton 对补丁的实现提出了建议，强调在受保护模式下不能简单地去掉某些函数，而是应该重用现有实现并确保安全性。此外，Kunwu Chan 在测试补丁时发现了一些混淆，主要与配置选项有关。经过进一步的沟通，Kunwu 确认了补丁的功能，并表示补丁在不同配置下的表现符合预期，最终为补丁添加了测试和审核标记。

总体来看，本周的讨论集中在补丁的实现细节和测试结果上，参与者们对如何确保补丁的有效性和安全性进行了深入交流。

#### 📝 邮件列表

1. **[07-17 23:47]** [PATCH 0/2] Dump instructions on panic for pKVM/nvhe
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[07-17 23:47]** [PATCH 1/2] KVM: arm64: Dump instruction on hyp panic
   - 发件人: Mostafa Saleh <smostafa@google.com>
3. **[07-24 23:51]** [PATCH 0/2] KVM: arm64: Destroy the stage-2 page-table periodically
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
4. **[07-24 23:51]** [PATCH 1/2] KVM: arm64: Split kvm_pgtable_stage2_destroy()
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
5. **[07-24 23:51]** [PATCH 2/2] KVM: arm64: Destroy the stage-2 page-table periodically
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
6. **[07-29 08:57]** Re: [PATCH 1/2] KVM: arm64: Split kvm_pgtable_stage2_destroy()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[07-29 09:01]** Re: [PATCH 2/2] KVM: arm64: Destroy the stage-2 page-table
 periodically
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[07-31 20:58]** Re: [PATCH 1/2] KVM: arm64: Dump instruction on hyp panic
   - 发件人: Kunwu Chan <kunwu.chan@linux.dev>
9. **[07-31 14:05]** Re: [PATCH 1/2] KVM: arm64: Dump instruction on hyp panic
   - 发件人: Mostafa Saleh <smostafa@google.com>
10. **[08-01 16:00]** Re: [PATCH 1/2] KVM: arm64: Dump instruction on hyp panic
   - 发件人: Kunwu Chan <kunwu.chan@linux.dev>

---

### Thread 6: [PATCH v8 0/7] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Sat, 19 Jul 2025 02:11:22 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构上支持 FF-A 1.2 及其 SEND_DIRECT2 ABI 的补丁集，共包含七个补丁。

**原始补丁内容**：
补丁集的核心是支持 FF-A 1.2 规范，该规范引入了新的 SEND_DIRECT2 ABI，允许使用寄存器 x4-x17 作为消息负载。补丁旨在防止主机使用比与虚拟机监控器（hypervisor）协商的更低版本的 FF-A，因为虚拟机监控器没有必要的兼容路径来转换版本。

**之前讨论要点**：
在历史讨论中，补丁的几个关键点包括：
1. 将 FF-A 1.2 接口标记为不支持，以避免错误转发。
2. 对 FFA_FEATURE 调用的响应进行掩码处理。
3. 将支持的 FF-A 版本提升至 1.2，为实现新的消息接口做准备。
4. 增加对 FFA_MSG_SEND_DIRECT_REQ2 的支持。

**本周的新讨论与进展**：
本周的讨论主要集中在补丁的确认与建议上。Will Deacon 对多个补丁表示认可（Acked-by），并提出了一些改进建议，例如希望 ffa_call_supported() 在 FF-A 版本低于 1.2 时返回 false，以提高代码的清晰度和可维护性。这些反馈将有助于进一步完善补丁集。

#### 📝 邮件列表

1. **[07-19 02:11]** [PATCH v8 0/7] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[07-19 02:11]** [PATCH v8 4/7] KVM: arm64: Mark optional FF-A 1.2 interfaces as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[07-19 02:11]** [PATCH v8 5/7] KVM: arm64: Mask response to FFA_FEATURE call
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
4. **[07-19 02:11]** [PATCH v8 6/7] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
5. **[07-19 02:11]** [PATCH v8 7/7] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
6. **[07-29 16:45]** Re: [PATCH v8 4/7] KVM: arm64: Mark optional FF-A 1.2 interfaces as
 unsupported
   - 发件人: Will Deacon <will@kernel.org>
7. **[07-29 16:46]** Re: [PATCH v8 5/7] KVM: arm64: Mask response to FFA_FEATURE call
   - 发件人: Will Deacon <will@kernel.org>
8. **[07-29 16:49]** Re: [PATCH v8 6/7] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Will Deacon <will@kernel.org>
9. **[07-29 16:54]** Re: [PATCH v8 7/7] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 7: [PATCH kvmtool v3 0/6] arm64: Nested virtualization support

**📧 邮件数**: 8 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 29 Jul 2025 10:57:39 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM64 嵌套虚拟化支持的补丁系列（[PATCH kvmtool v3 0/6]）。该补丁系列的主要目的是为 KVM 工具添加对 ARM64 嵌套虚拟化的支持。

在历史讨论中，补丁系列的 v3 版本进行了调整，主要更新了提交信息并添加了对 FEAT_E2H0 可用性的检查。补丁的内容包括更新内核头文件以支持新的 EL2 能力，添加命令行选项以允许 VCPU 在 EL2 中启动，以及支持 VGIC 设备控制等。

本周的新讨论中，Andre Przywara 提出了六个补丁的具体内容：
1. **补丁 1**：同步内核 UAPI 头文件以支持 ARM 嵌套虚拟化。
2. **补丁 2**：实现初步的嵌套虚拟化支持，允许用户通过命令行选项“--nested”在 EL2 启动来宾。
3. **补丁 3**：支持设置维护中断。
4. **补丁 4**：添加计数器偏移控制选项，便于测试定时器子系统。
5. **补丁 5**：支持 FEAT_E2H0，以便于一些旧版来宾的兼容。
6. **补丁 6**：生成 HYP 定时器中断规范。

Marc Zyngier 对该系列补丁表示了认可，并给予了审核意见。这些补丁的实施将显著增强 KVM 工具在 ARM64 架构上的虚拟化能力。

#### 📝 邮件列表

1. **[07-29 10:57]** [PATCH kvmtool v3 0/6] arm64: Nested virtualization support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
2. **[07-29 10:57]** [PATCH kvmtool v3 1/6] Sync kernel UAPI headers with v6.16
   - 发件人: Andre Przywara <andre.przywara@arm.com>
3. **[07-29 10:57]** [PATCH kvmtool v3 2/6] arm64: Initial nested virt support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
4. **[07-29 10:57]** [PATCH kvmtool v3 3/6] arm64: nested: add support for setting maintenance IRQ
   - 发件人: Andre Przywara <andre.przywara@arm.com>
5. **[07-29 10:57]** [PATCH kvmtool v3 4/6] arm64: add counter offset control
   - 发件人: Andre Przywara <andre.przywara@arm.com>
6. **[07-29 10:57]** [PATCH kvmtool v3 5/6] arm64: add FEAT_E2H0 support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
7. **[07-29 10:57]** [PATCH kvmtool v3 6/6] arm64: Generate HYP timer interrupt specifiers
   - 发件人: Andre Przywara <andre.przywara@arm.com>
8. **[07-29 11:03]** Re: [PATCH kvmtool v3 0/6] arm64: Nested virtualization support
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 8: [PATCH v9 0/6] KVM: arm64: Support FF-A 1.2

**📧 邮件数**: 7 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 30 Jul 2025 21:15:03 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上支持 FF-A（Firmware Framework for Arm）1.2 版本的补丁集。补丁集包含六个部分，主要目的是引入新的 SEND_DIRECT2 ABI，允许使用更多寄存器作为消息载荷，并确保主机不会使用低于已协商的 FF-A 版本。

在历史讨论中，补丁集的背景是 FF-A 1.2 规范的引入，强调了与超管（hypervisor）之间的版本兼容性问题。之前的讨论集中在如何更新 SMC（Secure Monitor Call）调用，以支持更多参数的传递，同时更新了不支持的接口列表。

本周的新讨论中，补丁集的具体实现细节得到了进一步的完善。主要进展包括：
1. 确保在主机尝试降级 FF-A 版本时返回正确的错误值。
2. 更新 FF-A 初始化和主机处理程序以使用 SMCCC 1.2，简化了实现。
3. 将 FF-A 通知接口标记为不支持，以避免错误的调用。
4. 将 FF-A 1.2 的可选接口标记为不支持，防止它们被错误代理。
5. 在处理 FFA_FEATURE 调用时，屏蔽响应中的额外位。
6. 将超管支持的 FF-A 版本提升至 1.2，以启用新的消息接口。

这些补丁经过测试，确保在 QEMU 下运行 Android 时能够成功使用 SEND_DIRECT2 ABI。整体上，这些更新旨在提高 KVM 的稳定性和兼容性。

#### 📝 邮件列表

1. **[07-30 21:15]** [PATCH v9 0/6] KVM: arm64: Support FF-A 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[07-30 21:15]** [PATCH v9 1/6] KVM: arm64: Correct return value on host version
 downgrade attempt
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[07-30 21:15]** [PATCH v9 2/6] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
4. **[07-30 21:15]** [PATCH v9 3/6] KVM: arm64: Mark FFA_NOTIFICATION_* calls as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
5. **[07-30 21:15]** [PATCH v9 4/6] KVM: arm64: Mark optional FF-A 1.2 interfaces as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
6. **[07-30 21:15]** [PATCH v9 5/6] KVM: arm64: Mask response to FFA_FEATURE call
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
7. **[07-30 21:15]** [PATCH v9 6/6] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>

---

### Thread 9: [PATCH v16 00/22] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs

**📧 邮件数**: 7 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 23 Jul 2025 11:46:52 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于KVM（Kernel-based Virtual Machine）的补丁系列，主要目的是为非CoCo虚拟机启用主机用户空间对guest_memfd支持的内存映射。Fuad Tabba 提出的补丁（PATCH v16 00/22）经过多次修改，简化了Kconfig选择和依赖关系，并确保在x86和arm64架构上始终启用guest_memfd。这一补丁的实施将支持如Firecracker等虚拟机管理程序完全基于guest_memfd的运行。

在历史讨论中，参与者们探讨了补丁的有效性及其对现有KVM功能的影响，特别是关于mmap支持的问题。Sean Christopherson指出，KVM在处理某些虚拟机类型时缺乏对guest_memfd的支持，导致了功能上的缺失。

在本周的新讨论中，Fuad确认了在其测试环境中，针对x86和arm64的自测通过，表示对Sean提出的补丁版本17没有异议，并表示感谢。这表明补丁的进展顺利，参与者们对后续版本的发布持积极态度。整体来看，讨论集中在补丁的有效性和后续版本的准备上，显示出社区对KVM功能扩展的关注和支持。

#### 📝 邮件列表

1. **[07-23 11:46]** [PATCH v16 00/22] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[07-23 11:47]** [PATCH v16 22/22] KVM: selftests: guest_memfd mmap() test when mmap
 is supported
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[07-24 15:15]** Re: [PATCH v16 22/22] KVM: selftests: guest_memfd mmap() test when
 mmap is supported
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[07-24 16:46]** Re: [PATCH v16 00/22] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs
   - 发件人: Ackerley Tng <ackerleytng@google.com>
5. **[07-25 07:56]** Re: [PATCH v16 00/22] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[07-28 08:00]** Re: [PATCH v16 22/22] KVM: selftests: guest_memfd mmap() test when
 mmap is supported
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[07-28 08:05]** Re: [PATCH v16 00/22] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 10: [PATCH v1 0/4] A couple of improvements for VMM to inject external
 abort to guest

**📧 邮件数**: 5 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 31 Jul 2025 21:20:00 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于改进虚拟机监控器（VMM）在处理外部中止时的补救措施的补丁集，共包含四个补丁（PATCH v1 0/4）。主要目标是允许用户空间通过 KVM_SET_VCPU_EVENTS API 注入外部指令和数据中止。

在历史讨论中，补丁的背景是 VMM 在处理同步外部指令或数据中止时，常常需要向客户机注入外部中止。当前的 KVM_SET_VCPU_EVENTS API 仅支持注入外部数据中止，因此需要扩展其功能。

本周的新讨论中，Jiaqi Yan 提出了补丁的具体内容：
1. 扩展 KVM_SET_VCPU_EVENTS API，以支持外部指令中止的注入。
2. 允许用户空间在注入同步外部中止（SEA）时提供 ESR_ELx 的值，以便将来可以支持 ESR_ELx.ISS2 的模拟。

补丁还涉及到 ABI 变更，讨论了是否需要引入新的 ABI 版本（如 exception_v2 或 kvm_vcpu_events_v2）。本周的讨论中，参与者们对补丁的实现细节进行了反馈，并对 ABI 变更的必要性进行了探讨。

最终，补丁集的更新文档也反映了这些变化，确保用户能够理解如何在用户空间中使用这些新功能。整体而言，本周的讨论推动了补丁集的进展，并为用户提供了更灵活的中止处理能力。

#### 📝 邮件列表

1. **[07-31 21:20]** [PATCH v1 0/4] A couple of improvements for VMM to inject external
 abort to guest
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
2. **[07-31 21:20]** [PATCH v1 1/4] KVM: arm64: Allow userspace to inject external
 instruction abort
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
3. **[07-31 21:20]** [PATCH v1 2/4] KVM: arm64: Allow userspace to supply ESR when
 injecting SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
4. **[07-31 21:20]** [PATCH v1 3/4] KVM: selftests: Test injecting external abort with ISS
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
5. **[07-31 21:20]** [PATCH v1 4/4] Documentation: kvm: update UAPI for injecting SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>

---

### Thread 11: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Sat, 19 Jul 2025 14:24:45 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（内核虚拟机）在 ARM64 架构上处理 SEA（系统错误处理）的补丁。补丁的主题为“[PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA”，旨在改进 KVM 在 ARM64 平台上的错误处理能力。

在历史讨论中，参与者 Oliver Upton 和 Jiaqi Yan 讨论了补丁的细节和后续版本的发布计划。Jiaqi Yan 提到，尽管新一代 ARM64 平台依然依赖 KVM 来更优雅地处理 SEA，缺乏 APEI（高级平台错误接口）的支持，因此希望尽快与上游社区达成共识并锁定提案。

在本周的新讨论中，Oliver Upton 提到他已发布了与 VNCR（虚拟网络控制寄存器）相关的修复，并建议 Jiaqi Yan 可以在即将发布的 kvmarm-6.17 版本上进行补丁的重基。Jiaqi Yan 随后确认已基于 VNCR 修复发布了补丁的 v3 版本，并在当前的 kvmarm/next 上进行了更新。

总结来说，本周的进展主要集中在补丁的版本更新和与 VNCR 修复的整合，显示出参与者之间的积极合作与沟通。

#### 📝 邮件列表

1. **[07-19 14:24]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
2. **[07-25 15:54]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
3. **[07-29 14:28]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[07-31 14:06]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>

---

### Thread 12: [PATCH v3 0/3] VMM can handle guest SEA via KVM_EXIT_ARM_SEA

**📧 邮件数**: 4 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 31 Jul 2025 20:58:41 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于处理虚拟机中的同步外部中止（SEA）的问题，提出了一系列补丁（PATCH v3 0/3），旨在通过 KVM_EXIT_ARM_SEA 让虚拟机监控程序（VMM）能够更好地处理此类事件。

**原始问题**：
当主机的 APEI 无法处理同步外部中止时，KVM 会直接向虚拟CPU注入异步 SError，通常会导致虚拟机内核崩溃。此问题在现代数据中心服务器中尤为常见，因为这些服务器通常会遇到可恢复的未更正内存错误（UER）。

**之前讨论要点**：
历史上，KVM 将 SEA 委托给 APEI 处理，但并非所有平台都支持此功能。当前的处理方式会导致虚拟机崩溃，因此需要一种更优雅的恢复机制。补丁建议将 SEA 重定向到 VMM，以便 VMM 可以更好地控制和处理这些错误。

**本周新讨论与进展**：
本周的讨论集中在补丁的具体实现上，包括：
1. **补丁内容**：引入了 KVM_CAP_ARM_SEA_TO_USER 和 KVM_EXIT_ARM_SEA 两个新特性，允许用户空间在处理 SEA 时接收更多信息。
2. **自测**：补丁中包含了自测试用例，验证 KVM 在 APEI 无法处理 SEA 时是否能正确返回 KVM_EXIT_ARM_SEA，并提供必要的错误信息。
3. **文档更新**：补丁还更新了相关文档，详细说明了新功能的使用方法和预期行为。

整体而言，这一系列补丁旨在提升 KVM 对 SEA 的处理能力，减少虚拟机因内存错误而崩溃的风险，同时增强用户空间对错误处理的控制能力。

#### 📝 邮件列表

1. **[07-31 20:58]** [PATCH v3 0/3] VMM can handle guest SEA via KVM_EXIT_ARM_SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
2. **[07-31 20:58]** [PATCH v3 1/3] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
3. **[07-31 20:58]** [PATCH v3 2/3] KVM: selftests: Test for KVM_EXIT_ARM_SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
4. **[07-31 20:58]** [PATCH v3 3/3] Documentation: kvm: new UAPI for handling SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>

---

### Thread 13: [PATCH] KVM: arm64: Set/unset vGIC v4 forwarding if direct IRQs are supported

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Jul 2025 22:37:10 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理 vGIC v4 转发的问题。原始的 patch 提出了在支持直接 IRQ 的情况下，设置或取消 vGIC v4 转发的功能。该 patch 的背景是之前的提交（commit <c652887a9288>）在处理 vGIC v4 初始化和拆除时，未能正确处理 KVM 设置或取消 vGIC v4 转发的情况，导致内核出现空指针解引用的错误，从而引发内核崩溃。

在本周的新讨论中，参与者 Raghavendra Rao Ananta 提出了修复方案，建议在设置或取消 vGIC v4 转发时，检查是否支持直接 IRQ。Oliver Upton 对此表示感谢，并建议进一步修改代码以确保在处理 vLPI 注入时，虚拟机具备 ITS（Interrupt Translation Service）。经过讨论，Raghavendra 确认了 Oliver 的修改建议，并表示将重新提交更新的 patch，Oliver 也同意进行后续的修改和提交。

总的来说，本周的讨论集中在修复内核崩溃问题的 patch 上，参与者们积极协作，提出了改进建议，并达成了下一步的行动计划。

#### 📝 邮件列表

1. **[07-28 22:37]** [PATCH] KVM: arm64: Set/unset vGIC v4 forwarding if direct IRQs are supported
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
2. **[07-29 07:37]** Re: [PATCH] KVM: arm64: Set/unset vGIC v4 forwarding if direct IRQs
 are supported
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[07-29 09:56]** Re: [PATCH] KVM: arm64: Set/unset vGIC v4 forwarding if direct IRQs
 are supported
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
4. **[07-29 11:02]** Re: [PATCH] KVM: arm64: Set/unset vGIC v4 forwarding if direct IRQs
 are supported
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 14: [PATCH] KVM: arm64: nv: Handle SEAs due to VNCR redirection

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 29 Jul 2025 11:23:42 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下处理由于 VNCR（虚拟网络控制寄存器）重定向引起的同步外部中止（SEA）的补丁。

**原始补丁内容**：
补丁的主要目的是在处理重定向到 VNCR 页的系统寄存器访问时，能够正确处理可能产生的外部中止。补丁通过调用 `kvm_handle_guest_sea()` 函数来处理这些中止，如果内核未能处理，则回退到虚拟错误（vSError）。此外，补丁还删除了一个不再需要的头文件 `kvm_ras.h`。

**之前讨论要点**：
在历史讨论中并没有具体的内容记录，但补丁的背景是为了增强 KVM 对于外部中止的处理能力，确保在发生错误时能够适当地响应。

**本周新讨论及进展**：
本周的讨论中，Oliver Upton 提交了补丁，并得到了 Marc Zyngier 的认可和审查。Marc 在回复中提到了一些意外的情况，并表示将会单独发布一个修复。Oliver 对此表示感谢，并确认会采纳 Marc 的修复建议。整体来看，本周的讨论主要集中在补丁的审查和后续修复的计划上，显示出社区对该补丁的积极反馈和进一步改进的意愿。

#### 📝 邮件列表

1. **[07-29 11:23]** [PATCH] KVM: arm64: nv: Handle SEAs due to VNCR redirection
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-30 10:54]** Re: [PATCH] KVM: arm64: nv: Handle SEAs due to VNCR redirection
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[07-30 10:34]** Re: [PATCH] KVM: arm64: nv: Handle SEAs due to VNCR redirection
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 15: [PATCH v5 0/6] KVM: arm64: Allow userspace to write GICD_TYPER2.nASSGIcap

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 23 Jul 2025 23:27:59 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下允许用户空间写入 GICD_TYPER2.nASSGIcap 的补丁（PATCH v5 0/6）。该补丁主要修复了 nASSGIreq 掩码的极性问题，并对一些细微的变更进行了明确说明。此外，补丁还涉及对 vSGIs 和 vLPIs 的支持区分、MAINT_IRQ 处理的整合、在初始化之前允许访问 GICD_IIDR 以及对 VGICv3 寄存器的文档描述。

在历史讨论中，参与者对补丁进行了多次修改和优化，确保了补丁的准确性和可读性。Oliver Upton 提出了补丁的最终版本，并得到了 Eric Auger 的审阅和认可。

在本周的新讨论中，Eric Auger 表达了对补丁的支持，并确认已进行审阅。Oliver Upton 随后宣布将该补丁应用到下一个版本中，并列出了补丁的具体内容和链接。这表明该补丁已获得通过，进入了后续的开发流程。

#### 📝 邮件列表

1. **[07-23 23:27]** [PATCH v5 0/6] KVM: arm64: Allow userspace to write GICD_TYPER2.nASSGIcap
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-28 18:07]** Re: [PATCH v5 0/6] KVM: arm64: Allow userspace to write
 GICD_TYPER2.nASSGIcap
   - 发件人: Eric Auger <eauger@redhat.com>
3. **[07-28 10:15]** Re: [PATCH v5 0/6] KVM: arm64: Allow userspace to write GICD_TYPER2.nASSGIcap
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 16: [PATCH] KVM: arm64: selftests: Add FEAT_RAS EL2 registers to get-reg-list

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Jul 2025 08:26:03 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM 的 arm64 自测中添加 FEAT_RAS EL2 寄存器到寄存器列表的补丁（patch）。该补丁的目的是将 VDISR_EL2 和 VSESR_EL2 寄存器添加到用户空间可见的嵌套虚拟机的寄存器列表中，以便更好地支持相关功能。

在历史讨论中没有提供具体的背景信息，但本周的讨论中，Oliver Upton 提出了该补丁，并在邮件中详细描述了所做的修改，包括在 `get-reg-list.c` 文件中添加了 VDISR_EL2 和 VSESR_EL2 寄存器的相关代码。Marc Zyngier 对该补丁表示认可，并给予了确认（Acked-by）。最终，Oliver Upton 在同一天的后续邮件中宣布该补丁已被应用到下一版本中。

本周的进展显示该补丁得到了积极的反馈，并顺利进入了代码库，标志着对 KVM arm64 自测功能的增强。

#### 📝 邮件列表

1. **[07-28 08:26]** [PATCH] KVM: arm64: selftests: Add FEAT_RAS EL2 registers to get-reg-list
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-28 16:47]** Re: [PATCH] KVM: arm64: selftests: Add FEAT_RAS EL2 registers to get-reg-list
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[07-28 10:15]** Re: [PATCH] KVM: arm64: selftests: Add FEAT_RAS EL2 registers to get-reg-list
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 17: [PATCH] KVM: arm64: ptdump: Fix exec attribute printing

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Sat,  2 Aug 2025 18:40:21 +0800

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，旨在修复页面表转储中可执行属性的打印问题。

1. **原始 patch/问题内容**：补丁的主要目的是修正当前客人阶段2页面表转储中可执行属性的打印方式。现有实现错误地将“X”标记为不可执行区域，而将可执行区域标记为空格。补丁通过交换这两个字符串来解决此问题。

2. **之前的讨论要点**：本线程没有历史讨论，所有内容均为本周的新讨论。

3. **本周的新讨论、进展或结论**：本周的讨论包括 Wei-Lin Chang 提出的补丁和 Anshuman Khandual 的回复。Wei-Lin Chang 详细说明了补丁的内容和目的，而 Anshuman Khandual 提出疑问，认为 KVM_PTE_LEAF_ATTR_HI_S2_XN 宏的语义已经是反向的，即当该宏被设置时，表示该条目不可执行，这与补丁的目的存在一定的矛盾。此讨论表明对补丁的理解和实现存在不同看法，可能需要进一步澄清和讨论。

#### 📝 邮件列表

1. **[08-02 18:40]** [PATCH] KVM: arm64: ptdump: Fix exec attribute printing
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
2. **[08-03 19:33]** Re: [PATCH] KVM: arm64: ptdump: Fix exec attribute printing
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 18: [PATCH] KVM: arm64: nv: Properly check ESR_EL2.VNCR on taking a VNCR_EL2 related fault

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 30 Jul 2025 11:18:28 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理 VNCR_EL2 相关故障的补丁。补丁的主要内容是修正对 ESR_EL2.VNCR 位的检查，之前的实现错误地测试了 ESR_EL2.DFSC 中的随机位，导致未能正确识别故障类型。Marc Zyngier 提出将 BUG_ON() 改为 WARN_ON_ONCE()，以避免在错误发生时导致系统崩溃。

在历史讨论中，虽然没有直接的邮件记录，但补丁的背景是基于之前的一个提交（069a05e535496），该提交处理了 VNCR_EL2 触发的故障。Marc 在审查相关补丁时发现了这个问题。

本周的新讨论中，Marc 提交了补丁，并得到了 Joey Gouly 的认可，表示已审查并同意该修改。这表明补丁得到了积极的反馈，可能会在后续版本中合并。整体来看，此次讨论集中在修复 KVM 的故障处理逻辑，以提高系统的稳定性和可靠性。

#### 📝 邮件列表

1. **[07-30 11:18]** [PATCH] KVM: arm64: nv: Properly check ESR_EL2.VNCR on taking a VNCR_EL2 related fault
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-31 11:07]** Re: [PATCH] KVM: arm64: nv: Properly check ESR_EL2.VNCR on taking a
 VNCR_EL2 related fault
   - 发件人: Joey Gouly <joey.gouly@arm.com>

---

### Thread 19: [PATCH v7 4/5] KVM: arm64: Bump the supported version of FF-A to
 1.2

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 18 Jul 2025 14:45:17 +0100

#### 🤖 AI 总结

在本次邮件讨论中，主题为“[PATCH v7 4/5] KVM: arm64: Bump the supported version of FF-A to 1.2”的补丁主要涉及将 KVM 对 FF-A 的支持版本提升至 1.2。历史讨论中，参与者 Per Larsen 提出该补丁需要拆分为更小的部分，因为它在一次性修改中包含了多个内容。此外，他质疑检查 a2[15:2] 和 a3 位的必要性，认为根据规范这些位应为“保留位”（MBZ），不应强制检查。Will Deacon 也同意将版本提升到 v1.2 的修改可以单独成补丁。

在本周的新讨论中，Marc Zyngier 对之前的观点进行了回应，强调在支持更高版本之前，必须确保 MBZ 位的检查，以避免未来版本中这些位被分配后产生的混淆。他认为，如果不强制检查这些位的值，将无法理解“客户端”所传达的含义，可能导致错误的实现。因此，他支持在当前版本中继续执行 MBZ 的检查。

总结来看，历史讨论集中在补丁的拆分和必要性上，而本周讨论则进一步明确了对 MBZ 位检查的立场，强调了其重要性。

#### 📝 邮件列表

1. **[07-18 14:45]** Re: [PATCH v7 4/5] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Will Deacon <will@kernel.org>
2. **[07-31 08:56]** Re: [PATCH v7 4/5] KVM: arm64: Bump the supported version of FF-A to 1.2
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 20: [PATCH v2] KVM: arm64: Move bundling vLPI and vSGI to vgic_supports_direct_msis()

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 29 Jul 2025 21:06:44 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在将 vLPI（虚拟本地中断）和 vSGI（虚拟共享中断）的捆绑逻辑移动到 `vgic_supports_direct_msis()` 函数中。

**原始补丁内容**：
补丁的目的是修复在 commit <c652887a9288> 中引入的一个问题，该问题导致在 KVM 设置或取消 vGIC v4 转发时出现内核崩溃。具体来说，错误发生在 vGIC v4 的初始化和拆卸过程中，未能正确处理 vLPI 和 vSGI 的捆绑逻辑。

**之前讨论要点**：
在历史讨论中，参与者们关注了该补丁的必要性和潜在影响，强调了在处理 vGIC v4 时需要确保系统的稳定性和可靠性。

**本周的新讨论与进展**：
本周的讨论中，Raghavendra Rao Ananta 对补丁的 changelog 进行了修改，并确认已将其应用于修复中。Oliver Upton 对此表示感谢，并确认补丁已成功提交到代码库。这标志着该问题的修复工作取得了实质性进展。

#### 📝 邮件列表

1. **[07-29 21:06]** [PATCH v2] KVM: arm64: Move bundling vLPI and vSGI to vgic_supports_direct_msis()
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
2. **[07-29 14:23]** Re: [PATCH v2] KVM: arm64: Move bundling vLPI and vSGI to vgic_supports_direct_msis()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 21: [PATCH 0/4] KVM: arm64: Userspace GICv3 sysreg access fixes and testing

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 18 Jul 2025 12:11:50 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 GICv3 系统寄存器访问修复和测试。历史讨论中，Marc Zyngier 提出了一个补丁集，旨在解决一个导致用户空间无法访问 ICH_HCR_EL2 寄存器的错误。该补丁集包含四个补丁：第一个修复了 sysreg 表的顺序问题，第二和第三个确保表的排序检查，最后一个补丁增强了 vgic_init 自测，确保可以访问这些寄存器。

在本周的新讨论中，Oliver Upton 确认已将这些补丁应用到下一个版本中，并感谢 Marc 的贡献。补丁的具体内容包括修复 ICH_HCR_EL2 的顺序、明确重置回调的检查、强制 GICv3 系统寄存器表的排序，以及添加基本的 GICv3 sysreg 用户空间访问测试。这些进展标志着对用户空间 GICv3 寄存器访问问题的有效解决。

#### 📝 邮件列表

1. **[07-18 12:11]** [PATCH 0/4] KVM: arm64: Userspace GICv3 sysreg access fixes and testing
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-28 10:15]** Re: [PATCH 0/4] KVM: arm64: Userspace GICv3 sysreg access fixes and testing
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 22: [PATCH v9 19/43] arm64: RME: Allow populating initial contents

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 31 Jul 2025 18:56:38 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM64 架构下的 RME（Runtime Memory Encryption）功能，具体是一个补丁（PATCH v9 19/43），旨在允许填充初始内容。此补丁的目的是增强对使用 hugetlb 页面（大页）的 guest_memfd 的支持，特别是在内存转换时进行就地转换。

在之前的讨论中，参与者提到了在内存转换过程中，KVM（Kernel-based Virtual Machine）对由 guest_memfd 提供的 folios（内存页的集合）进行引用计数的问题。由于在内存转换过程中需要拆分和合并这些 folios，因此希望避免 KVM 对这些页面的引用计数。讨论中提出了两种可能的解决方案：一是明确告知 guest_memfd 某个特定的物理页号（pfn）正在被 KVM 使用，二是将该页面标记为 hwpoisoned（硬件损坏）。

在本周的新讨论中，参与者 Steven Price 提出了对当前补丁的进一步思考，询问是否假设了对 guest 内存范围的双重备份，以及在 priv_pfn 和 pfn 相同的情况下，内存填充是否能与 CCA（Cache Coherent Architecture）正常工作。他对在支持就地转换的 guest_memfd 文件的情况下，内存填充的具体实现表示好奇。整体来看，本周的讨论集中在补丁的实现细节和潜在的技术挑战上。

#### 📝 邮件列表

1. **[07-31 18:56]** Re: [PATCH v9 19/43] arm64: RME: Allow populating initial contents
   - 发件人: Vishal Annapurve <vannapurve@google.com>

---

### Thread 23: [PATCH v3 05/15] KVM: x86: Add support for KVM userfault exits

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 30 Jul 2025 21:11:18 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 x86 架构下新增对用户故障退出（userfault exits）的支持，具体内容为一个补丁（PATCH v3 05/15）。

在历史讨论中，虽然没有提供具体的背景信息，但可以推测该补丁旨在改进 KVM 的内存管理，尤其是在处理用户故障时的表现。

在本周的新讨论中，参与者 James Houghton 提到该补丁在 `recover_huge_pages_range()` 函数中未能移除一个警告（WARN），这个警告可能会在启用 `KVM_MEM_LOG_DIRTY_PAGES` 和 `KVM_MEM_USERFAULT` 后，再禁用 `KVM_MEM_USERFAULT` 时被触发。他表示正在与 Sean 进行离线讨论，等待对 KVM_GENERIC_PAGE_FAULT 部分的重构。此外，他还计划花更多时间关注 QEMU 相关的工作。

总的来说，本周的讨论集中在补丁的具体实现问题上，特别是如何处理警告信息，以及与其他开发者的协作进展。

#### 📝 邮件列表

1. **[07-30 21:11]** Re: [PATCH v3 05/15] KVM: x86: Add support for KVM userfault exits
   - 发件人: James Houghton <jthoughton@google.com>

---

### Thread 24: [PATCH] Documentation: KVM: Use unordered list for pre-init VGIC registers

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 29 Jul 2025 08:22:42 -0700

#### 🤖 AI 总结

本邮件主题为“[PATCH] Documentation: KVM: Use unordered list for pre-init VGIC registers”，主要讨论了对 KVM 文档中 VGIC（虚拟通用中断控制器）寄存器预初始化部分的格式修正。

原始的 patch 旨在将一个单列表格转换为无序列表，但由于使用了错误的标记格式，导致文档构建失败。具体错误信息显示在 Sphinx 的并行构建中，提示存在意外的章节标题或过渡。

在之前的讨论中，未提及具体的内容或问题，因此本次邮件是首次提出的修复建议。

本周的讨论由 Oliver Upton 提出，修复了文档中的格式问题，将原本的表格格式改为无序列表，确保文档能够正确构建。修复后的代码在文档中用星号标记了寄存器字段，简化了格式并解决了构建错误。该 patch 由 Stephen Rothwell 报告，并已关闭相关链接。

总之，本周的进展是成功修复了文档构建问题，确保了 KVM 文档的准确性和可读性。

#### 📝 邮件列表

1. **[07-29 08:22]** [PATCH] Documentation: KVM: Use unordered list for pre-init VGIC registers
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 25: [PATCH 6.1.y] KVM: arm64: sys_regs: disable -Wuninitialized-const-pointer
 warning

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 28 Jul 2025 14:07:36 -0700

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在禁用 Clang 编译器的 -Wuninitialized-const-pointer 警告。

**原始补丁内容**：
Justin Stitt 提交的补丁针对 Clang 22 中出现的一个警告，该警告指出传递给 `get_clidr_el1()` 函数的 `clidr` 变量是一个未初始化的常量指针。虽然该函数实际上并不关心这个问题，因为它会忽略常量属性，但这个警告被认为是一个误报。补丁通过在 `Makefile` 中禁用该警告，避免了维护者的时间浪费和可能的构建问题。

**之前讨论要点**：
在本邮件中并没有提及历史讨论或补丁的背景信息，说明此补丁是首次提出。

**本周的新讨论与进展**：
本周的讨论主要集中在补丁的具体实现上，Justin Stitt 详细描述了补丁的必要性及其实现方式，强调该补丁只适用于 6.1 版本，因为在 6.2 及之后的版本中，该代码段已被重构。补丁的提交也提到，类似的补丁已为 5.15 版本发送。

总之，此补丁的目的是解决编译时的误报问题，确保代码的稳定性和可维护性。

#### 📝 邮件列表

1. **[07-28 14:07]** [PATCH 6.1.y] KVM: arm64: sys_regs: disable -Wuninitialized-const-pointer
 warning
   - 发件人: Justin Stitt <justinstitt@google.com>

---

## 📌 RFC

共 2 个 thread

---

### Thread 1: [RFC PATCH v1 00/38] ARM CCA Device Assignment support

**📧 邮件数**: 115 | **👥 参与者**: 9 | **📅 开始时间**: Mon, 28 Jul 2025 19:21:37 +0530

#### 🤖 AI 总结

本邮件线程讨论了 ARM CCA 设备分配支持的 RFC PATCH（版本 1，共 38 个补丁）。以下是主要内容的总结：

1. **原始补丁内容**：该补丁系列实现了 ARM CCA 架构中的设备分配支持，基于 Alp12 规范进行代码更改，扩展了 TSM 框架，使其在主机和客户机中均可使用。补丁中详细描述了设备分配的工作流程，包括主机和客户机的步骤。

2. **历史讨论要点**：之前的讨论集中在如何实现设备分配的细节、TSM 的工作流程以及如何处理设备的锁定和解锁状态。参与者们讨论了如何确保设备在不同状态下的安全性和有效性，特别是在 T=1 和 T=0 模式下的设备交互。

3. **本周的新讨论与进展**：本周的讨论主要围绕补丁的具体实现和潜在问题展开。参与者提出了对 DMA 分配、设备通信、设备状态管理等方面的建议和疑问。Jason Gunthorpe 和 Jonathan Cameron 对补丁的设计提出了批评和建议，强调了在实现过程中需要考虑的安全性和性能问题。此外，Aneesh Kumar K.V 针对补丁中的问题进行了回应，并表示将根据反馈进行修改。

总的来说，本次讨论聚焦于 ARM CCA 设备分配的实现细节、潜在的安全隐患以及如何在不同的设备状态下进行有效管理。参与者们积极交流，提出了许多建设性的意见。

#### 📝 邮件列表

1. **[07-28 19:21]** [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
2. **[07-28 19:21]** [RFC PATCH v1 01/38] tsm: Add tsm_bind/unbind helpers
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
3. **[07-28 19:21]** [RFC PATCH v1 02/38] tsm: Move tsm core outside the host directory
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
4. **[07-28 19:21]** [RFC PATCH v1 03/38] tsm: Move dsm_dev from pci_tdi to pci_tsm
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
5. **[07-28 19:21]** [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private memory
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
6. **[07-28 19:21]** [RFC PATCH v1 05/38] tsm: Don't overload connect
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
7. **[07-28 19:21]** [RFC PATCH v1 06/38] iommufd: Add and option to request for bar mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
8. **[07-28 19:21]** [RFC PATCH v1 07/38] iommufd/viommu: Add support to associate viommu with kvm instance
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
9. **[07-28 19:21]** [RFC PATCH v1 08/38] iommufd/tsm: Add tsm_op iommufd ioctls
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
10. **[07-28 19:21]** [RFC PATCH v1 09/38] iommufd/vdevice: Add TSM Guest request uAPI
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
11. **[07-28 19:21]** [RFC PATCH v1 10/38] iommufd/vdevice: Add TSM map ioctl
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
12. **[07-28 19:21]** [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform device
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
13. **[07-28 19:21]** [RFC PATCH v1 12/38] coco: host: arm64: CCA host platform device driver
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
14. **[07-28 19:21]** [RFC PATCH v1 13/38] coco: host: arm64: Create a PDEV with rmm
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
15. **[07-28 19:21]** [RFC PATCH v1 14/38] coco: host: arm64: Device communication support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
16. **[07-28 19:21]** [RFC PATCH v1 15/38] coco: host: arm64: Stop and destroy the physical device
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
17. **[07-28 19:21]** [RFC PATCH v1 16/38] X.509: Make certificate parser public
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
18. **[07-28 19:21]** [RFC PATCH v1 17/38] X.509: Parse Subject Alternative Name in certificates
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
19. **[07-28 19:21]** [RFC PATCH v1 18/38] X.509: Move certificate length retrieval into new helper
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
20. **[07-28 19:21]** [RFC PATCH v1 19/38] coco: host: arm64: set_pubkey support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
21. **[07-28 19:21]** [RFC PATCH v1 20/38] coco: host: arm64: Add support for creating a virtual device
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
22. **[07-28 19:21]** [RFC PATCH v1 21/38] coco: host: arm64: Add support for virtual device communication
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
23. **[07-28 19:21]** [RFC PATCH v1 22/38] coco: host: arm64: Stop and destroy virtual device
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
24. **[07-28 19:22]** [RFC PATCH v1 23/38] coco: guest: arm64: Update arm CCA guest driver
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
25. **[07-28 19:22]** [RFC PATCH v1 24/38] arm64: CCA: Register guest tsm callback
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
26. **[07-28 19:22]** [RFC PATCH v1 25/38] cca: guest: arm64: Realm device lock support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
27. **[07-28 19:22]** [RFC PATCH v1 26/38] KVM: arm64: Add exit handler related to device assignment
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
28. **[07-28 19:22]** [RFC PATCH v1 27/38] coco: host: arm64: add RSI_RDEV_GET_INSTANCE_ID related exit handler
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
29. **[07-28 19:22]** [RFC PATCH v1 28/38] coco: host: arm64: Add support for device communication exit handler
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
30. **[07-28 19:22]** [RFC PATCH v1 29/38] coco: guest: arm64: Add support for collecting interface reports
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
31. **[07-28 19:22]** [RFC PATCH v1 30/38] coco: host: arm64: Add support for realm host interface (RHI)
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
32. **[07-28 19:22]** [RFC PATCH v1 31/38] coco: guest: arm64: Add support for fetching interface report and certificate chain from host
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
33. **[07-28 19:22]** [RFC PATCH v1 32/38] coco: guest: arm64: Add support for guest initiated TDI bind/unbind
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
34. **[07-28 19:22]** [RFC PATCH v1 33/38] KVM: arm64: CCA: handle dev mem map/unmap
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
35. **[07-28 19:22]** [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range found in the interface report
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
36. **[07-28 19:22]** [RFC PATCH v1 35/38] coco: guest: arm64: Add Realm device start and stop support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
37. **[07-28 19:22]** [RFC PATCH v1 36/38] KVM: arm64: CCA: enable DA in realm create parameters
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
38. **[07-28 19:22]** [RFC PATCH v1 37/38] coco: guest: arm64: Add support for fetching device measurements
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
39. **[07-28 19:22]** [RFC PATCH v1 38/38] coco: guest: arm64: Add support for fetching device info
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
40. **[07-28 11:08]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
41. **[07-28 11:10]** Re: [RFC PATCH v1 07/38] iommufd/viommu: Add support to associate
 viommu with kvm instance
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
42. **[07-28 11:17]** Re: [RFC PATCH v1 10/38] iommufd/vdevice: Add TSM map ioctl
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
43. **[07-28 11:33]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
44. **[07-29 13:53]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
45. **[07-29 13:58]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
46. **[07-29 14:00]** Re: [RFC PATCH v1 07/38] iommufd/viommu: Add support to associate
 viommu with kvm instance
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
47. **[07-29 14:07]** Re: [RFC PATCH v1 10/38] iommufd/vdevice: Add TSM map ioctl
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
48. **[07-29 11:29]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
49. **[07-29 11:31]** Re: [RFC PATCH v1 10/38] iommufd/vdevice: Add TSM map ioctl
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
50. **[07-29 11:33]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
51. **[07-29 17:26]** Re: [RFC PATCH v1 07/38] iommufd/viommu: Add support to associate
 viommu with kvm instance
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
52. **[07-29 17:34]** Re: [RFC PATCH v1 08/38] iommufd/tsm: Add tsm_op iommufd ioctls
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
53. **[07-29 18:10]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm
 platform device
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
54. **[07-29 18:22]** Re: [RFC PATCH v1 12/38] coco: host: arm64: CCA host platform
 device driver
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
55. **[07-29 20:16]** Re: [RFC PATCH v1 07/38] iommufd/viommu: Add support to associate
 viommu with kvm instance
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
56. **[07-29 20:19]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
57. **[07-29 20:22]** Re: [RFC PATCH v1 12/38] coco: host: arm64: CCA host platform device
 driver
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
58. **[07-30 14:43]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Xu Yilun <yilun.xu@linux.intel.com>
59. **[07-30 14:55]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Xu Yilun <yilun.xu@linux.intel.com>
60. **[07-30 14:12]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm
 platform device
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
61. **[07-30 14:28]** Re: [RFC PATCH v1 12/38] coco: host: arm64: CCA host platform
 device driver
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
62. **[07-30 11:09]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
63. **[07-30 11:25]** Re: [RFC PATCH v1 12/38] coco: host: arm64: CCA host platform
 device driver
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
64. **[07-30 11:28]** Re: [RFC PATCH v1 12/38] coco: host: arm64: CCA host platform
 device driver
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
65. **[07-30 11:38]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm
 platform device
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
66. **[07-30 13:23]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm
 platform device
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
67. **[07-30 13:39]** Re: [RFC PATCH v1 13/38] coco: host: arm64: Create a PDEV with rmm
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
68. **[07-30 15:07]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Greg KH <gregkh@linuxfoundation.org>
69. **[07-30 14:52]** Re: [RFC PATCH v1 14/38] coco: host: arm64: Device communication
 support
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
70. **[07-30 14:57]** Re: [RFC PATCH v1 15/38] coco: host: arm64: Stop and destroy the
 physical device
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
71. **[07-30 15:08]** Re: [RFC PATCH v1 19/38] coco: host: arm64: set_pubkey support
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
72. **[07-30 15:12]** Re: [RFC PATCH v1 20/38] coco: host: arm64: Add support for
 creating a virtual device
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
73. **[07-30 15:13]** Re: [RFC PATCH v1 21/38] coco: host: arm64: Add support for virtual
 device communication
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
74. **[07-30 15:15]** Re: [RFC PATCH v1 22/38] coco: host: arm64: Stop and destroy
 virtual device
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
75. **[07-30 15:22]** Re: [RFC PATCH v1 23/38] coco: guest: arm64: Update arm CCA guest
 driver
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
76. **[07-30 15:26]** Re: [RFC PATCH v1 24/38] arm64: CCA: Register guest tsm callback
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
77. **[07-30 15:32]** Re: [RFC PATCH v1 25/38] cca: guest: arm64: Realm device lock
 support
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
78. **[07-30 15:35]** Re: [RFC PATCH v1 26/38] KVM: arm64: Add exit handler related to
 device assignment
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
79. **[07-30 15:43]** Re: [RFC PATCH v1 30/38] coco: host: arm64: Add support for realm
 host interface (RHI)
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
80. **[07-30 15:46]** Re: [RFC PATCH v1 31/38] coco: guest: arm64: Add support for
 fetching interface report and certificate chain from host
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
81. **[07-30 15:51]** Re: [RFC PATCH v1 32/38] coco: guest: arm64: Add support for guest
 initiated TDI bind/unbind
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
82. **[07-30 16:06]** Re: [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range
 found in the interface report
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
83. **[07-30 13:03]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
84. **[07-31 11:16]** Re: [RFC PATCH v1 37/38] coco: guest: arm64: Add support for
 fetching device measurements
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
85. **[07-31 11:36]** Re: [RFC PATCH v1 38/38] coco: guest: arm64: Add support for
 fetching device info
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
86. **[07-31 11:40]** Re: [RFC PATCH v1 35/38] coco: guest: arm64: Add Realm device start
 and stop support
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
87. **[07-31 14:39]** Re: [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range
 found in the interface report
   - 发件人: Arto Merilainen <amerilainen@nvidia.com>
88. **[07-31 14:47]** Re: [RFC PATCH v1 13/38] coco: host: arm64: Create a PDEV with rmm
   - 发件人: Arto Merilainen <amerilainen@nvidia.com>
89. **[07-31 09:11]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
90. **[07-31 09:17]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
91. **[07-31 09:22]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
92. **[07-31 09:26]** Re: [RFC PATCH v1 12/38] coco: host: arm64: CCA host platform device
 driver
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
93. **[07-31 09:28]** Re: [RFC PATCH v1 14/38] coco: host: arm64: Device communication
 support
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
94. **[07-31 09:29]** Re: [RFC PATCH v1 23/38] coco: guest: arm64: Update arm CCA guest
 driver
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
95. **[07-31 14:22]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm
 platform device
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
96. **[07-31 14:48]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
97. **[07-31 14:54]** Re: [RFC PATCH v1 23/38] coco: guest: arm64: Update arm CCA guest
 driver
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
98. **[07-31 13:44]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
99. **[07-31 13:46]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
100. **[07-31 13:53]** Re: [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range
 found in the interface report
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
101. **[07-31 19:07]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: dan.j.williams <dan.j.williams@intel.com>
102. **[08-01 10:31]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Greg KH <gregkh@linuxfoundation.org>
103. **[08-01 10:30]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
104. **[08-01 11:53]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
105. **[08-01 12:51]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
106. **[08-01 14:19]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: dan.j.williams <dan.j.williams@intel.com>
107. **[08-01 17:54]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: dan.j.williams <dan.j.williams@intel.com>
108. **[08-02 14:14]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
109. **[08-02 14:33]** Re: [RFC PATCH v1 08/38] iommufd/tsm: Add tsm_op iommufd ioctls
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
110. **[08-02 16:24]** Re: [RFC PATCH v1 13/38] coco: host: arm64: Create a PDEV with rmm
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
111. **[08-02 16:27]** Re: [RFC PATCH v1 13/38] coco: host: arm64: Create a PDEV with rmm
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
112. **[08-02 10:41]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
113. **[08-02 11:17]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
114. **[08-02 16:50]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: dan.j.williams <dan.j.williams@intel.com>
115. **[08-03 19:26]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>

---

### Thread 2: [RFC PATCH 06/34] KVM: gunyah: Add initial Gunyah backend
 support

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 01 Aug 2025 13:25:43 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）中 Gunyah 后端支持的初步补丁（RFC PATCH 06/34）。该补丁旨在为 KVM 提供对 Gunyah 虚拟化后端的支持，强调了内核应提供一个通用的虚拟化 API，以适应不同的硬件和固件。

在历史讨论中，虽然没有具体的邮件记录，但可以推测出参与者对这一补丁的概念表示支持，认为内核的角色是提供统一的虚拟化接口，而不是局限于特定的实现。

在本周的新讨论中，参与者 David Woodhouse 提出了对补丁的看法，认为内核应减少条件编译（#ifdef）的使用，借鉴 x86 架构中静态调用（static_calls）的模型。他建议可以创建一个灵感来源于 x86 的模型，允许通过不同的“低虚拟化层”（lowvisor）操作集来提供某些方法，包括本地 KVM、pKVM、Gunyah 和 CCA 等。他希望能将这些不同的实现结合起来，以便在保持 KVM 用户空间 API 尽可能统一的同时，减少对系统的干扰。

总的来说，本周的讨论集中在如何优化和统一虚拟化 API 方面，提出了对补丁的具体改进建议。

#### 📝 邮件列表

1. **[08-01 13:25]** Re: [RFC PATCH 06/34] KVM: gunyah: Add initial Gunyah backend
 support
   - 发件人: David Woodhouse <dwmw2@infradead.org>

---

## 📌 Bug Report

共 2 个 thread

---

### Thread 1: [Bug Report] external_aborts failure related to efa1368ba9f4 ("KVM:
 arm64: Commit exceptions from KVM_SET_VCPU_EVENTS immediately")

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 21 Jul 2025 07:00:00 -0700

#### 🤖 AI 总结

本邮件线程讨论了与 KVM（Kernel-based Virtual Machine）相关的一个 bug 报告，具体涉及到 commit efa1368ba9f4 的问题，该 commit 旨在立即提交 KVM_SET_VCPU_EVENTS 的异常。

在历史讨论中，Jiaqi Yan 提出了一个 bug 报告，指出在进行 SEA 注入开发时，工具测试文件 `external_aborts.c` 在其本地跟踪的 kvmarm/next 分支中失败，具体表现为测试断言失败，导致程序中断。Marc Zyngier 随后提供了一个相关的 commit 链接，建议进行检查。

在本周的新讨论中，Jiaqi Yan 确认 Marc Zyngier 提供的 commit 修复了他所遇到的问题，并对此表示感谢。这表明之前的讨论和修复工作取得了积极进展，问题得到了有效解决。

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
4. **[07-29 11:33]** Re: [Bug Report] external_aborts failure related to efa1368ba9f4
 ("KVM: arm64: Commit exceptions from KVM_SET_VCPU_EVENTS immediately")
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>

---

### Thread 2: [bug report] KVM: arm64: Add a range to __pkvm_host_unshare_guest()

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 22 Jul 2025 13:59:06 +0100

#### 🤖 AI 总结

在本次邮件讨论中，主题为“[bug report] KVM: arm64: Add a range to __pkvm_host_unshare_guest()”。历史讨论中，Ben Horgan 提出了一个问题：在使用透明大页（transparent huge pages）启动 pkvm 客户机时，系统崩溃，错误信息显示在 `arch/arm64/kvm/hyp/nvhe/mem_protect.c` 的第 1088 行。Ben 提出了一份补丁，修复了 `__pkvm_host_relax_perms_guest()` 函数中的问题，使其能够正确处理块映射，从而避免崩溃。

在本周的新讨论中，Quentin Perret 对 Ben 的补丁表示认可，并指出该补丁的思路是正确的。然而，他也提到在 `__pkvm_host_mkyoung_guest()` 函数中存在类似的问题，建议将其中的 `PAGE_SIZE` 替换为 `0`，以解决同样的潜在错误。Quentin 感谢 Ben 提出的报告，并对后续的修复工作表示期待。

总结来看，历史讨论中提出的补丁有效解决了 pkvm 启动时的崩溃问题，而本周的讨论则进一步发现了相关函数中的类似问题，推动了修复工作的进展。

#### 📝 邮件列表

1. **[07-22 13:59]** [bug report] KVM: arm64: Add a range to __pkvm_host_unshare_guest()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[07-28 15:38]** Re: [bug report] KVM: arm64: Add a range to
 __pkvm_host_unshare_guest()
   - 发件人: Quentin Perret <qperret@google.com>

---

## 📌 Selftest

共 1 个 thread

---

### Thread 1: KVM selftest for L2 guest execution fails

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 30 Jul 2025 15:44:48 +0900

#### 🤖 AI 总结

本邮件线程讨论了 KVM 自测试在 L2 客户端执行时失败的问题。Itaru Kitayama 提出了一个测试代码，运行在 kvmarm/next 的 NV2+VHE 环境下，测试时出现了资源暂时不可用的错误，导致 KVM_RUN 失败。测试代码中涉及了虚拟化和嵌套支持的设置，但在执行时遇到了问题。

Marc Zyngier 对 Itaru 的代码进行了批评，指出代码中存在多个问题，例如启用了 S2 转换但未进行相关设置、在设置了 TGE 的情况下尝试返回 EL1，以及设置了 NV 但未填充 VNCR_EL2。他建议 Itaru 从一个简单的 L2 开始，不要在客户机中使用 NV，确保有正确的 HCR_EL2 配置后再进行更复杂的设置。

在本周的讨论中，Itaru 感谢了 Marc 的反馈，并表示将遵循他的建议进行修改。整体来看，讨论集中在 KVM 自测试的配置和实现细节上，Marc 提出的问题和建议将帮助 Itaru 改进测试代码。

#### 📝 邮件列表

1. **[07-30 15:44]** KVM selftest for L2 guest execution fails  
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>
2. **[07-30 13:24]** Re: KVM selftest for L2 guest execution fails  
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[07-31 06:40]** Re: KVM selftest for L2 guest execution fails  
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 changes for 6.17, round #1

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Jul 2025 11:17:35 -0700

#### 🤖 AI 总结

本邮件线程讨论了 KVM/arm64 在 6.17 版本的首次变更，主要由 Oliver Upton 提出。此次变更包含了多个重要更新，尤其是 GICv5 主机驱动的引入，支持下一代 ARM64 中断控制器，涵盖中断路由、MSI、干扰翻译等功能。此外，还包括对 GICv3 虚拟机在 GICv5 硬件上的虚拟化支持，以及用户空间对 GICv3 特性的控制等。

在历史讨论中，虽然没有具体的历史邮件，但本周的讨论显示出 Oliver 和 Paolo 之间的有效沟通。Oliver 提到的变更已被 Paolo 成功拉取，并且在后续的邮件中，Oliver 还提到了一处文档标记的错误，要求在变更基础上进行修复。Paolo 随后确认已完成修复。

总的来说，本周讨论的重点是 KVM/arm64 的新特性和修复，特别是 GICv5 的引入及其相关支持，显示出社区对 ARM64 虚拟化技术的持续关注与改进。

#### 📝 邮件列表

1. **[07-28 11:17]** [GIT PULL] KVM/arm64 changes for 6.17, round #1
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-29 19:12]** Re: [GIT PULL] KVM/arm64 changes for 6.17, round #1
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>
3. **[07-29 10:17]** Re: [GIT PULL] KVM/arm64 changes for 6.17, round #1
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[07-29 19:48]** Re: [GIT PULL] KVM/arm64 changes for 6.17, round #1
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

